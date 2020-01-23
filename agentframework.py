#This wholly builds agents and initializes their class and moves the object
import random
class drunks:
    
#initializing the agents and their environment
    
    def __init__(self,drunks , house, environment): 
        self.drunks = drunks
        self.environment=environment
        self.house = house
        

    
class Location(object):
    def __init__(self, x, y):
        #x and y are numbers
        self.x = random.randint(140,150)
        self.y = random.randint(150,160)
        #created to move agents to and fro
    def move(self): 
        
        if random.random() < 0.5:
            self.x= (self.x+1)% 300 
        else :
            self.x=(self.x-1)%300
        
        if random.random() < 0.5:
             self.y= (self.y+1) % 300
        else :
            self.y=(self.y-1) %300 
            
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
