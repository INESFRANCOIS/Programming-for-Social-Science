# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:08:22 2020
Agent class
@author: Inès
@ version : 1.0.6
"""

# Importation of the random module 
import random
# Importation of module testmod in the librairie doctest 
from doctest import testmod


random.seed

# Creation of the Agent class 
class Agent:
    
    # Constructor 
    
    def __init__(self, name, environment, agents, y, x):
        
        """
        Function to initialize the attributes of the Agent class.

        Parameters
        ----------
        name : str
             Label for the different variables   
        environment : a list of lists
            the environment in which the agents are located
        agents : list
        y : Number
            y-cordinate of the agent 
        x : Number
            x_coordinate of the agent
                    
        Returns
        -------
        None
        """
               
        self.name = name
        self.y = y
        self.x = x
        self.environment = environment
        self.agents = agents
        self.store = random.randint(0,100)
        
        
    # Method to move
  
    def change(self, d, x, dim):
        
        """
        Function to change the value.

        Parameters
        ----------
        d : Number
            value to be added or subtracted.
        x : Number
            Value to be added to.
        dim : Number
            Ensures the result is between 0 and dim.

        Returns
        -------
        x : Number
            x plus or minus d.
            
        Testing code    
        >>> random.seed(0)
        >>> a = Agent(0,0,0,0,0)
        >>> a.change(1, 40, 100)
        40
        >>> a.change(1, 40, 100)
        41        
        >>> a.change(1, 25, 100)
        25       
        >>> a.change (1,25,100)
        24
        
        """
                
        r = random.random()
        if r < 0.5:
            r = random.random()
            if r < 0.5:
                x = (x + d) % dim
            else:
                x = (x - d) % dim
        return x
    
        if __name__ =='__main__':
          import doctest
          doctest.testmod () 
    
    def move(self, d):
    
        """
        Function to move.

        Parameters
        ----------
        d : Number
            Value to be added or substracted in the change function
        
        Returns
        -------
        None
        
        Testing code
        >>> agents = []
        >>> environment = []
        >>> row = []
        >>> row.append(7)
        >>> environment.append(row)
        >>> a = Agent(0,environment,0,3,4)
        >>> a.move(1)
        >>> a.y 
        3
        >>> a.x
        0
        
        """    
        
        self.y = self.change(d, self.y, len(self.environment))
        self.x = self.change(d, self.x, len(self.environment[0]))

     
    # Method to eat
  
           
    def eat(self):
        
        """
        Function to simulate the eating behaviour.

        Parameters
        ----------
        store : Number
            Resources of the agent.
        amount : Number
            Number of foods which are in the environment.

        Returns
        -------
        None
    
        Testing code
        >>> random.seed(0)
        >>> environment = []
        >>> row = []
        >>> row.append(7)
        >>> environment.append(row)
        >>> a = Agent(0,environment,0,0,0)
        >>> a.store
        49
        >>> a.eat()
        >>> a.store
        56
        
        """
    
        amount = self.environment[self.y][self.x]
        if amount > 10:
           self.store += 10
           self.environment[self.y][self.x] = self.environment[self.y][self.x] - 10
        else :
           self.store += amount
           self.environment[self.y][self.x] = 0
        amount = self.environment[self.y][self.x]
                
    # Method to share 
    
    def distance_between(self, agent):
        
        """
        Function to calculate the distance between two agents 

        Parameters
        ----------
        agent :list
            An instance of Agent.
        
        Returns
        -------
        Distance between self and x.  
        
        Testing code
        >>> a = Agent(0,0,0,0,0)
        >>> b = Agent(0,0,0,3,4)
        >>> a.distance_between(b)
        5.0
        """
            
        return (((self.y - agent.y)**2) + ((self.x - agent.x)**2))**0.5
    
        
    def share_with_neighbours(self, neighbourhood):
        
        """
        Function to simulate the food sharing.

        Parameters
        ----------
        neighbourhood : Number
            Defined maximal distance (20) for which agent can share their foods. 
       
        Returns
        -------
        None
        
        Testing code
        >>> random.seed (0)
        >>> agents = []
        >>> neighbourhood = 20
        >>> a = Agent(0,0,agents,0,0)
        >>> a.store
        49
        >>> agents.append(a)
        >>> b = Agent(0,0,agents,0,0)
        >>> b.store
        97
        >>> agents.append(b)
        >>> a.share_with_neighbours(neighbourhood)
        >>> b. share_with_neighbours (neighbourhood)
        >>> a.store
        49
        >>> b.store
        97
        
        """
 
        for agent in self.agents:
            distance = self.distance_between(agent)
            s1 = self.store 
            s2 = agent.store 
            if distance <= neighbourhood:
                if s1 < s2:
                    t = s1 + s2
                    s1 = (2/3)* t
                    s2 = (1/3)* t
                elif s1 > s2 :
                    t = s1 + s2
                    s1 = (1/3)* t
                    s2 = (2/3)* t 
                
                

