import random
class Agent:

	def __init__(self):
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

