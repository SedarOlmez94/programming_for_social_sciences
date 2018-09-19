import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import sys

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
        ((agents_row_a._y - agents_row_b._y)**2))**0.5
environment = []
''' We pass the arguments for iterations, agents and neighbourhood when executing
    the script.'''
num_of_iterations = int(sys.argv[1])
num_of_agents = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
agents = []

#Lines here happen before any data is processed
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    # Lines here happen before each row is proceessed
    for value in row:
        # do something with values
        rowlist.append(value)
    # Lines here happen after row is processed
    environment.append(rowlist)
# Lines here happen after all the data  is processed
f.close()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


# print (agents)
# agentA = agentframework.Agent(environment, agents)
# agentA.get_agent(0)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
