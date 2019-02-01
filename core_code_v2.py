# Libraries:
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import sys
matplotlib.use('PS')

# Global variables:
environment = []
''' We pass the arguments for iterations, agents and neighbourhood when executing
    the script.'''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
num_of_iterations = 500
num_of_agents = 10
neighbourhood = 5
poacher_neighbourhood = 5
agents = []
poacher = agentframework.Agent(environment, agents)
kill_count = 0

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
            agents[-1].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            matplotlib.pyplot.annotate(agents[i].share_with_neighbours(neighbourhood), (agents[i]._x,agents[i]._y), (agents[i]._x,agents[i]._y+2))
            matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color = "white")
            print(agents[i]._x,agents[i]._y)

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.annotate("POACHER", (agents[-1]._x,agents[-1]._y), (agents[-1]._x,agents[-1]._y+2))
    matplotlib.pyplot.scatter(agents[-1]._x,agents[-1]._y, color = "black")
    assassinate()
    matplotlib.pyplot.text(45, 105, "KILLS: " +str(kill_count), bbox=dict(facecolor='red', alpha=0.5), fontsize = 15)

def gen_function():
    """The generate function loops the simulation until the `number of iterations` is met."""
    a = 0
    while (a < num_of_iterations):
        yield a			# Returns control and waits next call.
        a = a + 1

def assassinate():
    """A special method used to allow the poacher agent to shoot any sheep in its proximity and remove it
        from the agents[] list."""
    global num_of_agents
    global kill_count
    poacher_agent = agents[-1]
    for i in range(num_of_agents):
        if (poacher_agent.distance_between(agents[i]) <= poacher_neighbourhood):
            matplotlib.pyplot.arrow(poacher_agent._x,poacher_agent._y, agents[i]._x, agents[i]._y,color = "red")
            num_of_agents = num_of_agents - 1
            kill_count = kill_count + 1
            del agents[i]

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

#Add poacher to the list of agents.
agents.append(poacher)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()
print (kill_count)
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
