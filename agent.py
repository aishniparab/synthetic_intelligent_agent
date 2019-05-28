from pprint import pprint

class Agent:
	def __init__(self, sensors, connection):
		self.sensors = sensors #count
		self.connection = connection #same, opposite, simple
		self.speed = 0 #init speed is 0
		self.pos = (0, 0)

	def test(self):
		print({"sensors": self.sensors, "connection": self.connection, "speed": self.speed})
	
	def behaviour(self):
		if self.connection == "simple":

class Environment:
	def __init__(self, size, stimuli, agent):
		self.grid = [[0 for i in range(size)] for j in range(size)]
		self.grid[0][0] = stimuli
		agent.pos = (size/2, size/2)
		self.grid[size/2][size/2] = "A"
	
	def render(self):
		pprint(self.grid)

def main():
	basic = Agent(1, "simple")
	env = Environment(5, "S", basic)
	print basic.test()
	print env.render()
	print basic.pos

if __name__ == "__main__":
    main()