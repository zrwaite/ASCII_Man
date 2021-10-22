import random
from sprite import Sprite
from dot import Dot #Makes dot syntax for dictionary
def err_input(msg, limits): 
    '''Takes user input and throws/handles errors'''
    while(True):
        try:
            value=int(input(msg))#Stores input
            if (value < limits[0] or value > limits[1]):#only takes input within limit
                return -1
            return value
        except:
            return -1
class Character(Sprite):
    '''Character class is used to represent the user's sprite, inherits from Sprite'''
    def __init__(self, draw="", x=0, y=0):
        '''Initializes character by calling parent __init__, then generates random body'''
        super().__init__(draw, x, y) #Calls parent constructor
        self.heads=["( )","[ ]","{ }"] #Head options
        self.faces=["ⴶ","⍥","⍛","⍨","ꗸ","⸪","ഋ"] #Face options that I found looking though every single unicode character in terminal
        self.torsos=["░","▒","▓"] #Torso options i found as stated above
        self.arms=["╒ ╕","❲ ❳","⟆ ⟅","⸨ ⸩","⡟ ⢻","⸔ ⸕","/ \\","ᖰ ᖳ"] #Arm options i found as stated above
        self.legs=["╿ ╿","⎥ ⎢","| |","⣸ ⣇","⥿ ⥿","⎠ ⎝","⎦ ⎣", " ∏ "] #Leg options i found as stated above
        self.head=self.heads[random.randint(0, len(self.heads)-1)] #Head starts as random head
        self.face=self.faces[random.randint(0, len(self.faces)-1)] #Face starts as random face
        self.torso=self.torsos[random.randint(0, len(self.torsos)-1)] #Torso starts as tandom torso
        self.arm=self.arms[random.randint(0, len(self.arms)-1)] #Arm starts as random arm
        self.leg=self.legs[random.randint(0, len(self.legs)-1)] #Leg starts as random leg
        self.draw=[[],[],[]] #Character is three lines long, so 2 d array
        self.set_body() #Sets full body with body parts
        self.size.y=len(self.draw) #Sets sizes
        self.size.x=len(self.draw[0])
        print("Make edits to the character: ")
        self.editor() #Prompts user to make edits to character 
    def editor_display(self):
        '''Shows current character to user and edit options'''
        output =  "╔═════╗ 0: Head -"+self.head
        output+="\n║ "+self.draw[0]+" ║ 1: Face - "+self.face
        output+="\n║ "+self.draw[1]+" ║ 2: Arms -"+self.arm
        output+="\n║ "+self.draw[2]+" ║ 3: Torso - "+self.torso
        output+="\n╚═════╝ 4: Legs -"+self.leg
        output+="\nAny other key: Done"
        return output
    def editor(self): 
        '''Allows the user to change character values'''
        complete=False
        while(not complete): #Until user is done
            print(self.editor_display()) #Print current character and instructions
            feature=err_input("Select feature to change (0-4): ", [0,4]) #User selects feature to edit
            #Based on feature specified, increments that feature to the next value in the available list
            if (feature==0):self.head=self.inc_feature(self.heads, self.head)
            elif (feature==1):self.face=self.inc_feature(self.faces, self.face)
            elif (feature==2):self.arm=self.inc_feature(self.arms, self.arm)
            elif (feature==3):self.torso=self.inc_feature(self.torsos, self.torso)
            elif (feature==4):self.leg=self.inc_feature(self.legs, self.leg)
            else:break
            self.set_body() #Sets full body to new value
        print("Edits complete!")
    def set_body(self): 
        '''Sets drawing values with available body parts'''
        self.draw[0]=self.head[0]+self.face+self.head[2] 
        self.draw[1]=self.arm[0]+self.torso+self.arm[2]
        self.draw[2]=self.leg
    def inc_feature(self, array, feature): 
        '''Uses lists of body part options, and moves to the next feature'''
        i=array.index(feature)+1 
        if (i>=len(array)):i=0
        return array[i] #Returns value of next element in list, or 1st value if end of list

