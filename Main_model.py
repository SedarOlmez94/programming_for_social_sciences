import random as random_number
import numpy as np
from scipy.spatial import distance
# Algorithm to be implemented: 

# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.

# Variables:
y0 = random_number.randint(0, 100)
x0 = random_number.randint(0, 100)
y1 = random_number.randint(0, 100)
x1 = random_number.randint(0, 100)
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

print("Agent 1: Position of y: " + str(generate_position(y0)))
print("Agent 1: Position of y: " + str(generate_position(y0)))
print("Agent 1: Position of x: " + str(generate_position(x0)))
print("Agent 1: Position of x: " + str(generate_position(x0)))


print("Agent 2: Position of y: " + str(generate_position(y1)))
print("Agent 2: Position of y: " + str(generate_position(y1)))
print("Agent 2: Position of x: " + str(generate_position(x1)))
print("Agent 2: Position of x: " + str(generate_position(x1)))


#Calculating the euclidean distance between two agents, I run the distance over 100 times for various results
while case_check != True:
	diff_y_coor = (distance.euclidean(generate_position(y0), generate_position(y1)))**2
	diff_x_coor = (distance.euclidean(generate_position(x0), generate_position(x1)))**2
	answer = (diff_y_coor + diff_x_coor)**0.5
	print(answer)
	pointer = pointer + 1
	if pointer == 100:
		case_check = True
	

# answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 could have been used. 
#for x in range(101):
#	print (answer)




