#Sheep_munch version 1

# Libraries:
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import sys
matplotlib.use('macosx')

# Global variables:
environment = []
''' We pass the arguments for iterations, agents and neighbourhood when executing
    the script.'''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
num_of_iterations = 200
num_of_agents = 10
neighbourhood = 10

agents = []


# Methods:
def distance_between(agents_row_a, agents_row_b):
    """Calculates the distance between two agents, used the pythagoras theory."""
    return (((agents_row_a._x - agents_row_b._x)**2) +
        ((agents_row_a._y - agents_row_b._y)**2))**0.5

def update(frame_number):
    """The update function animates the plain so agents move, eat and poacher shoots.
    Matplot was used heavily for the backend and front-end of the simulation."""
    fig.clear()
    global num_of_agents
    global environment

    for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            matplotlib.pyplot.annotate(agents[i].share_with_neighbours(neighbourhood), (agents[i]._x,agents[i]._y), (agents[i]._x,agents[i]._y+2))
            matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color = "white")
            print(agents[i]._x,agents[i]._y)

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

def gen_function():
    """The generate function loops the simulation until the `number of iterations` is met."""
    a = 0
    while (a < num_of_iterations):
        yield a			# Returns control and waits next call.
        a = a + 1

"""Here we read the data from the in.txt file to produce the environment map. Pixelation."""
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

# Add the agents to the agents[] list
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
