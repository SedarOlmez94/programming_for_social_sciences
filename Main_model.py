import random as random_number
# Algorithm to be implemented: 

# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.

# Variables:
y0 = 50
x0 = 50
y1 = 50
x1 = 50

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
