from pprint import pprint
import collections

class Agent:
	def __init__(self, sensors, connection):
		self.sensors = sensors #count
		self.connection = connection #same, opposite, simple
		self.speed = 0 #init speed is 0
		self.pos = (0, 0)

	#def behaviour(self):
		#if self.connection == "simple":

	
	def find_path(self, env, start):
         visited, queue = set([start]), collections.deque([[start]])
         while queue:
         	path = queue.popleft()
         	x, y = path[-1]
         	if env.grid[y][x] == env.goal:
         		return path
         	for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
	            if 0 <= x2 < env.width and 0 <= y2 < env.height and env.grid[y2][x2] != env.wall and (x2, y2) not in visited:
	                queue.append(path + [(x2, y2)])
	                visited.add((x2, y2))

class Environment:
	def __init__(self, agent):
		self.grid = [['*', 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
		self.wall = "#"
		self.clear = "."
		self.goal = "*"
		self.width = 5
		self.height = 5
		self.stimuli_pos = (0,0)
		agent.pos = (self.width/2, self.height/2)
	
	def render(self, grid):
		pprint(grid)

def main():
	basic = Agent(1, "simple")
	env = Environment(basic)
	
	env.render(env.grid)
	path = basic.find_path(env, basic.pos)
	
	for pos in path:
		grid_copy = env.grid[:]
		grid_copy[pos[0]][pos[1]] = "a"
		env.render(env.grid) 

if __name__ == "__main__":
    main()