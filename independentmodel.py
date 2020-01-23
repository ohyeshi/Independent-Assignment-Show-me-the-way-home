
"""
Created on Wed Jan 14 21:06:23 2020

@author: Oyeshi
"""

import numpy as np
import matplotlib.pyplot as plt
import agentframework
import matplotlib.animation

#defining agents
total_drunks = 25
drunks =[]
house = 25
pub=1
coordinates=[]

#Calling the  drunkplan file
Field = np.genfromtxt(r"C:\Users\Oyeshi\Documents\GIS DataBase\Proggramming_5990\Assignment_2\drunkplan", delimiter= ',')

#Displays pubs and homes
f = open(r"C:\Users\Oyeshi\Documents\GIS DataBase\Proggramming_5990\Assignment_2\drunkplan")
environment = []
for row in f:
    parsed_row = str.split(row, ",")
    rowlist=[]
    for value in parsed_row:
            rowlist.append(float(value))
    environment.append(rowlist)
f.close()
for a in range (300):
    for b in range (300):
        if environment[a][b] == 1:
            environment[a][b]= 100


for i in range (total_drunks):
    drunks.append(agentframework.drunks(drunks,house, environment))
    
       
for i in range (total_drunks):    
    house = (i+1)*10
    drunks.append(agentframework.drunks(drunks, house, environment))
    

    plt.imshow(environment) 
plt.show


for i in range(total_drunks):
   
    #creating scatterplots of the agents defined above
    plt.scatter(drunks[i].x,drunks[i].y) 
    plt.draw()   
    
    carry_on = True	
  
def distance_between(self, drunks):
    return (((self.x - drunks.x)**2) + ((self.y - drunks.y)**2))**0.5

while total_drunks>0:
     house+=1
     total_drunks-=1


def update(frame_number):
    
    fig.clear()
    
    
    
    for j in range(coordinates):
        for i in range(total_drunks):
            drunks[i].move()
            drunks[i].add()

#plotting values of x and y   
    plt.xlim(0,300)  
    plt.ylim(0,300) 
#plot the background    
    plt.imshow(environment) 
    
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < coordinates) & (carry_on) :
        yield a			
        a = a + 1
    
#code for animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
   
    
    plt.show()
    #plotting final raster
#run
    
