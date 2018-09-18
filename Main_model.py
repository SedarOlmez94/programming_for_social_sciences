import random as random_number
import numpy as np
import operator as op
import matplotlib.pyplot
from scipy.spatial import distance

# Variables:
agents = []
number_of_agents = 10
number_of_iterations = 100
for i in range(number_of_agents):
	agents.append([random_number.randint(0, 99), random_number.randint(0, 99)])
furthest_east_agent = []
case_check = False
pointer = 0

''' The for loop ensures a torus around the plain, that way agents always appear
within plain.'''
for i in range(number_of_agents):
	if random_number.random() < 0.5:
		agents[i][0] = (agents[i][0] + 1) % 100
	else:
		agents[i][0] = (agents[i][0] - 1) % 100



#Calculating the euclidean distance between the agents, I run the distance over 100 times for experimentation.
while case_check != True:
	diff_y_coor = distance.euclidean(agents[0][0], agents[1][0])
	diff_x_coor = distance.euclidean(agents[0][1], agents[1][1])
	answer = (diff_y_coor + diff_x_coor)**0.5
	print(answer)
	pointer = pointer + 1
	if pointer == number_of_iterations:
		case_check = True

#Here we plot the results of the agent's destination on the plain, the east most agent is painted red.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(number_of_agents-1):
	matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
furthest_east_agent = max(agents)
matplotlib.pyplot.scatter(furthest_east_agent[0], furthest_east_agent[1], color='red')
matplotlib.pyplot.show()
