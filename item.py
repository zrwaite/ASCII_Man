import random
from sprite import Sprite
from dot import Dot #Makes dot syntax for dictionary
class Item(Sprite): 
    '''Character class is used to represent the user's sprite, inherits from Sprite'''
    def __init__(self, draw="", x=0, y=0):
        '''Initializes character by calling parent __init__, 
        then generates random item with given lifespan and point values'''
        super().__init__(draw, x, y)
        self.dead=False #For 'garbage cleanup'
        self.points=random.randint(0,1) #Random items are worth 0 or 1 points
        self.lifespan=8 #Random items have a lifespan of 8 game frames
        if (not draw): #If draw isn't defined, it is a random item from the list below:
            draws=["<", ">", "~", "@", "%", "&", "*", "-", "+", "?", "!", "$"]
            self.draw=draws[random.randint(0, len(draws)-1)]
        if (self.draw=="-"): # - means lose 1 point, and lasts a long time
            self.points=-1
            self.lifespan=15
        elif (self.draw=="+"): # + means gain 1 point, and lasts a long time
            self.points=1
            self.lifespan=15
        elif (self.draw=="?"): # ? means lose 0 or 1 points, or gain up to 3 points. Lasts a while
            self.points=random.randint(-1,3)
            self.lifespan=10
        elif (self.draw=="!"): # ! means gain 3 points, lasts a normal amount of time
            self.points=3
            self.lifespan=8
        elif (self.draw=="$"): # $ means gain 5 points (woohoo) but doesn't last very long
            self.points=5
            self.lifespan=6
    def dec_lifespan(self): 
        '''Remaining lifespan decreases each time frame'''
        self.lifespan-=1
        if (not self.lifespan):self.dead=True #If it is out of time, it dies.
    def update(self, x, y):
        self.dec_lifespan()
        self.random(x, y)
    def is_dead(self): 
        '''Checks if item is 'dead' '''
        return self.dead
    def get_points(self): 
        '''Returns number of points for the item'''
        return self.points