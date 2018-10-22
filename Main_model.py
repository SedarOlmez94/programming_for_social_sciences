import random as random_number
import numpy as np
import operator as op
import matplotlib.pyplot
import time
from scipy.spatial import distance

# Variables:
agents = []
number_of_agents = 20
number_of_iterations = 100
pointer = 0
#furthest_east_agent = []
for i in range(number_of_agents):
	agents.append([random_number.randint(0, 99), random_number.randint(0, 99)])
#Methods
def calculate_euclidean_distance(agents_row_a, agents_row_b):
	pythagoras = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
	return pythagoras

''' The for loop ensures a torus around the plain, that way agents always appear
within plain. Agent movement is achieved.'''
for j in range(number_of_iterations):
	for i in range(number_of_agents):
		if random_number.random() < 0.5:
			agents[i][0] = (agents[i][0] + 1) % 100
		else:
			agents[i][0] = (agents[i][0] - 1) % 100
		if random_number.random() < 0.5:
			agents[i][1] = (agents[i][1] + 1) % 100
		else:
			agents[i][1] = (agents[i][1] - 1) % 100


#Calculating the euclidean distance between the agents, I run the distance over 100 times for experimentation.
#while case_check != True:
#for j in range(number_of_iterations):
start = time.clock()
for i in range(number_of_agents-1):
	distance = calculate_euclidean_distance(agents[i], agents[i+1])
	print (distance)
end = time.clock()
print("time = " + str(end - start))
	#pointer = pointer + 1
	#if pointer == number_of_iterations:
	#	case_check = True

#Here we plot the results of the agent's destination on the plain, the east most agent is painted red.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(number_of_agents-1):
	matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#furthest_east_agent = max(agents)
#matplotlib.pyplot.scatter(furthest_east_agent[0], furthest_east_agent[1], color='black')
m = max(agents, key=op.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='black')
matplotlib.pyplot.show()
