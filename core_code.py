import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import sys
matplotlib.use('macosx')


environment = []
''' We pass the arguments for iterations, agents and neighbourhood when executing
    the script.'''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
num_of_iterations = int(sys.argv[1])
num_of_agents = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
agents = []

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
        ((agents_row_a._y - agents_row_b._y)**2))**0.5

def update(frame_number):

    fig.clear()

    for i in range(num_of_agents):
            agents[i].move()

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
        print(agents[i]._x,agents[i]._y)

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
# matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.imshow(environment)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
#     #print(agents[i]._x,agents[i]._y)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
