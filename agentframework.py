import random

class Agent:

	def __init__(self, environment, agents):
		self.environment = environment
		self.agents = agents
		self.store = 0
		self._x = random.randint(0,99)
		self._y = random.randint(0,99)

	# Move the agents.
	def move(self):
		if random.random() < 0.5:
			self._y = (self._y + 1) % 100
		else:
			self._y = (self._y - 1) % 100
		if random.random() < 0.5:
			self._x = (self._x + 1) % 100
		else:
			self._x = (self._x - 1) % 100

	def eat(self):
		if self.environment[self._y][self._x] > 10:
			self.environment[self._y][self._x] -= 10
			self.store += 10

	def get_agent(self, index_of_agent):
		self.agents[index_of_agent]
		print (self.agents[index_of_agent])

	def share_with_neighbours(self, neighbourhood):
		for agents in self.agents:
			distance = self.distance_between(agents)
			if distance <= neighbourhood:
				sum = self.store + agents.store
				avg = sum /2
				self.store = avg
				agents.store = avg
				return ("Neighbour distance: " + str(distance))

	def distance_between(self, agent):
		return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
