import random as random_number
import numpy as np
from scipy.spatial import distance
import operator as op
import matplotlib.pyplot

# Variables:
agents = []
agents.append([random_number.randint(0, 99), random_number.randint(0, 99)])
agents.append([random_number.randint(0, 99), random_number.randint(0, 99)])
furthest_east_agent = []
case_check = False
pointer = 0

#Methods: 
def generate_position(value1):
	if random_number.random() < 0.5:
		value1 = value1 + 1
	else:
		value1 = value1 - 1
	return value1

#Main: 

# print("Agent 1: Position of y: " + str(generate_position(y0)))
# print("Agent 1: Position of y: " + str(generate_position(y0)))
# print("Agent 1: Position of x: " + str(generate_position(x0)))
# print("Agent 1: Position of x: " + str(generate_position(x0)))


# print("Agent 2: Position of y: " + str(generate_position(y1)))
# print("Agent 2: Position of y: " + str(generate_position(y1)))
# print("Agent 2: Position of x: " + str(generate_position(x1)))
# print("Agent 2: Position of x: " + str(generate_position(x1)))


#Calculating the euclidean distance between two agents, I run the distance over 100 times for various results
while case_check != True:
	diff_y_coor = distance.euclidean(generate_position(agents[0][0]), generate_position(agents[1][0]))
	diff_x_coor = distance.euclidean(generate_position(agents[0][1]), generate_position(agents[1][1]))
	answer = (diff_y_coor + diff_x_coor)**0.5
	print(answer)
	pointer = pointer + 1
	if pointer == 100:
		case_check = True

# print (max(agents))
furthest_east_agent = max(agents)
# print (furthest_east_agent[0])

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(furthest_east_agent[1], furthest_east_agent[0], color='red')
matplotlib.pyplot.show()
# print(max(agents, key=op.itemgetter(1)))
# print (agents)
# print (max(agents))
# answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 could have been used. 
#for x in range(101):
#	print (answer)























