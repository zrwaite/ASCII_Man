import random
from dot import Dot #Makes dot syntax for dictionary
class Sprite(object):
    '''Used to represent sprite objects that exist on the game screen'''
    def __init__(self, draw="", x=0, y=0):
        '''Initializes character with its look and position, with default parameters'''
        self.pos=Dot({ #Position is stored as Dot dictionary with x and y, that can 
            "x": int(x), #So that it can be accessed as pos.y and pos.x
            "y": int(y)  #This is how I am used to it so thought it would be cool to add it in
            })
        self.draw=[[draw]] #The drawing a 2d array, so that it can be modelled on the 2d plane, even though it is likely 1x1
        self.size=Dot({
            "y": len(self.draw), #Size is stored as Dot dictionary for size.x and size.y
            "x": len(self.draw[0]),
            })
    def left(self): 
        '''Moves the sprite left if there is space'''
        if(self.pos.x):self.pos.x-=1
    def right(self,r): #Moves
        '''Moves the sprite right if there is space'''
        if(self.pos.x+self.size.x<r):self.pos.x+=1
    def up(self):
        '''Moves the sprite up if there is space'''
        if(self.pos.y):self.pos.y-=1
    def down(self,b):
        '''Moves the sprite down if there is space'''
        if(self.pos.y+self.size.y<b):self.pos.y+=1
    def random(self, r, b):
        '''Determines range in which sprite can move,
        and moves the sprite to a random position within
        the limits of its current location'''
        x_range=[-1,1] #X-axis range starts as -1 to 1
        y_range=[-1,1] #Y-axis range starts as -1 to 1
        if(not self.pos.x):x_range[0]=0 #If pos.x=0, its lowest x-change is 0
        if(self.pos.x+self.size.x>=r-1):x_range[1]=0#If pos.x is game width, its highest x-change is 0
        if(not self.pos.y):y_range[0]=0 #If pos.y=0, its lowest y-change is 0
        if(self.pos.y+self.size.y>=b-1):y_range[1]=0 #If pos.y is game width, its highest y-change is 0
        self.pos.x+=random.randint(x_range[0], x_range[1]) #Moves to random x position within range
        self.pos.y+=random.randint(y_range[0], y_range[1]) #Moves to random y position within range
    def get_pos(self, axis=None):
        '''Returns position based on axis inputted'''
        if(axis=="y"): return self.pos.y
        elif(axis=="x"): return self.pos.x
        else: return self.pos
    def get_size(self, axis=None):
        '''Returns size based on axis inputted'''
        if(axis=="y"): return self.size.y
        elif(axis=="x"): return self.size.x
        else: return self.size
    def get_draw(self): 
        '''Returns sprite drawing'''
        return self.draw


