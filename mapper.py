import random
from dot import Dot 

class Mapper(object):
    '''Stores a game map, and outputs results based on inputs'''
    def __init__(self, x=30, y=15):
        '''Takes dimesions for game screen, with defaults 30x15'''
        try:
            self.x=int(x) if x>=5 else 5 #Minimum size of 5
            self.y=int(y) if y>=5 else 5
        except TypeError:
            self.x=5
            self.y=5
    def build_map(self, sprites): #Sprites is list of pairs with a dictionary  Pos, then value [pos{x:0,y:0},["+"]]
        '''Generates a new output based on given '''
        output="\n╔"+"═"*self.x+"╗\n" #Top row ╔═══╗
        for i in range(self.y): #For each row
            row=0 #Length of the row that has been printed
            output+="║" #Row starts with ║ 
            while (row<self.x+1): #While the row hasn't been filled
                if((sprites) and (sprites[0][0].y==i)):#If there is a sprite in the list and it is in the row(Always calls first sprite)
                    output+=" "*(sprites[0][0].x-row)+sprites[0][1] #Add empty spaces until its position, then add it
                    row+=sprites[0][0].x-row+len(sprites[0][1]) #Add the amount printed to the amount of the row that has been printed
                    del sprites[0] #Delete sprite that was just called
                else:
                    output+=" "*(self.x-row)+"║\n" #ends row with empty spaces and a ║
                    row=self.x+1 #Row is completed
        output+="╚"+"═"*self.x+"╝\n" #Bottom row╚═══╝
        return output #Returns screen to be printed
#borders=["═","║","╔","╗","╚","╝","╠","╣","╦","╩","╬"] 
#I am keeping this comment in case I use these borders in the future