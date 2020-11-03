# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:13:37 2020
Model which simulates the behaviours of agents in the environment
@author: Inès
@version : 1.0.6
"""

# Importation of librairies and modules 
import requests
import bs4
from bs4 import BeautifulSoup as soup
import matplotlib
matplotlib.use('TkAgg')
import tkinter
from tkinter import *
import matplotlib.pyplot
import matplotlib.figure
import matplotlib.animation 
import ABMagentclass
import random
import csv


# Initialyse the environment
environment = []
# Open the cvs file 
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
f. close()

# Initialyse the generator of randomized number  
random.seed(0)

# Initialyse the number of agents, iterations and frames 
num_of_agents = 10
num_of_iterations = 1
num_of_frames = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Get the page 
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html',verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

carry_on = True	

def init_func (self, y, x, agents):
    """
     Function to initiate the first image of the animation with initial agents. 

        Parameters
        ----------
        y: Number
            y coordinate of the agent
        x: Number 
            x coordinate of the agent
        agents: list 
             list of ten agents with their initial coordinates    
        Returns
        -------
        None 
    """
    
    global carry_on
    # Create the agents
    print ("Initial agents")
    print("name x y store")
    for i in range(num_of_agents):
        self.y = int(td_ys[i].text)
        self.x = int(td_xs[i].text)
        self.agents = agents.append(ABMagentclass.Agent(i, environment, agents, y, x))
        print(agents[i].name, agents[i].x, agents[i].y, agents[i].store)
          


def update(frame_number): 
     
    """
        Function to create a new image for the animation.

        Parameters
        ----------
        num_of_frames: Number
            Number of frames 
        
        Returns
        -------
        None 
        
    """
    print("frame_number",frame_number)
    
    fig.clear() 
    
    global carry_on
    # The agents move, eat and communicate
    for j in range(num_of_iterations): 
        random.shuffle (agents) # In each iteration, the order of agents is modified. 
        # Move agents
        for i in range(num_of_agents):
            agents[i].move(1)
        # Agents eat    
        for i in range(num_of_agents):
            agents[i].eat()
        # Agents share    
        for i in range(num_of_agents):
            agents[i].share_with_neighbours(neighbourhood)
    
    # Stop when all agents have store > 100
    n = 0
    print("name x y store")
    for i in range(num_of_agents):
        print(agents[i].name, agents[i].x, agents[i].y, agents[i].store)
        if (agents[i].store > 100):
            n += 1
            
    if (n == num_of_agents):
        carry_on = False
        print("n == num_of_agents stopping condition", frame_number)
        
     
    # Plot
    matplotlib.pyplot.imshow(environment) # Plot the enviornment
    for i in range(num_of_agents):        
        matplotlib.pyplot.scatter(agents[i].x , agents[i].y)
        #print((agents[i].x,agents[i].y))
        
        
def gen_function(b = [0]):
    a = 0
    global carry_on 
    print("carry_on", carry_on)
    while (a < num_of_frames) & (carry_on) :
        yield a			
        a = a + 1
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
   
# Create a window 
root = tkinter.Tk()
# Give a title for our window
root.wm_title("Model")
# Create a frame widget
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
# Show it onto the screen
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
tkinter.mainloop()

