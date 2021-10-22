#Name: Zac Waite
#Date: April 4 2021
#Program Name: game.py
#Purpose: Driver file for several classes that combine to create a 
#simple game that runs in terminal. Game allows user to create a 
#character and try to collect items within a given time frame

from pynput.keyboard import Listener, Key
#https://pypi.org/project/pynput/
#I read documentation here for python key events
import time
import random
from character import Character
from mapper import Mapper
from item import Item
from dot import Dot

def bub_sort_sprites(sprites): 
    '''Bubble sorts the sprites by their y and x coordinates, in that order'''
    for a in range(len(sprites)):#  loop to control number of passes
        for b in range(0,len(sprites)-1):#  loop to control number of comparisons for length of list-1
            #If the next value is bigger (y value is multiplied by 1000 because take precedent over x)
            if (sprites[b][0].y*1000+sprites[b][0].x)>(sprites[b+1][0].y*1000+sprites[b+1][0].x): 
                sprites[b],sprites[b+1]=sprites[b+1],sprites[b] #Flip the value with the one after it.
def gameover(sprites): 
    '''When the game is out of time'''
    global points, canvas #Print final score and final game screen 
    print("Time left  : 0 seconds")
    print("Final score:",points,"points")
    print(canvas.build_map(sprites)) 
    exit() #Quit program
def draw(): 
    '''Renders and draws new game screen'''
    global canvas, sprite, points, items, start_time
    overlap_items=[] #List of indexes of items that overlap with character, to take points from and delete
    for i in range(len(items)): #For all items, check for overlap
        if (sprite.get_pos("x")<=items[i].get_pos("x") and 
            sprite.get_pos("x")+sprite.get_size("x")>=items[i].get_pos("x") and 
            sprite.get_pos("y")<=items[i].get_pos("y") and 
            sprite.get_pos("y")+sprite.get_size("y")>=items[i].get_pos("y")):
            overlap_items.append(i) #If overlap, add index to list
    list_len=len(overlap_items) #Take list length or overlapping items
    for i in range(list_len): #Adds points from that item to total points, then deletes item
        points+=items[overlap_items[list_len-1-i]].get_points() #Add points from the object overlapped
        del items[overlap_items[list_len-1-i]] #Delete items at specified index backwards, to not mess up indexes
    sprites=[[sprite.get_pos(), sprite.get_draw()]] #Start list of sprites to render with user sprite
    for i in range(len(items)): #Go through each game item
        draw = items[i].get_draw() if isinstance(items[i].get_draw(), list) else [items[i].get_draw()] #converts draw to list
        sprites.append([items[i].get_pos(), draw]) #Adds item position and drawing as a list into the sprite list
    a=0
    #Reduces multi-line drawings into single-line chunks to be rendered
    while (a<len(sprites)): #For all sprite drawings
        if (len(sprites[a][1]))>1: #If the sprite drawing spans multiple lines
            for b in range(len(sprites[a][1])): #For each line
                new_pos=Dot({
                    "x":sprites[a][0].x,
                    "y":sprites[a][0].y,
                }) 
                new_pos.y+=b #New position is the same x, but y position is split between lines
                sprites.append([new_pos,[sprites[a][1][b]]]) #Add section of drawing with new y position
            del sprites[a] #Delete old multi-line drawing
            a-=1 #Go down one index, since deleted value
        a+=1 #Increment loop
    for i in range(len(sprites)):sprites[i][1]=sprites[i][1][0] #converts single-line lists into strings
    bub_sort_sprites(sprites) #Sort sprites for proper rendering
    i=0 #Deletes items in the same location
    while (i<len(sprites)-1): #For each item but the last
        if (sprites[i][0]==sprites[i+1][0]): #If the item is in the same spot as the next
            del sprites[i] #Delete item 
            i-=1 #Go down one index, since deleted value
        i+=1 #Increment loop
    time_left=int(61-(time.time()-start_time)) #Time left is 60 seconds minus the time since starting
    if(time_left<=0):gameover(sprites) #If no time left, run gameover function
    #Output info and game screen to the user
    print("Time left:", time_left, "seconds")
    print("Points   :", points)
    print(canvas.build_map(sprites))
def create_item(): 
    '''Creates new items (maybe)'''
    global canvas_x, canvas_y, items
    if (random.randint(0,1)): #50% chance of new item
        buffer=random.randint(random.randint(0,2) , random.randint(3,4)) #Move items from the edge, since they tend to stay there
        x=random.randint(buffer, canvas_x-buffer) #Set x position for new item
        y=random.randint(buffer, canvas_y-buffer) #Set y position for new item
        items.append(Item("", x, y)) #Add new item to list
def update_items(): 
    '''Updates all items in item list'''
    global items, canvas_x, canvas_y
    for i in range(len(items)): items[i].update(canvas_x, canvas_y) #Call the update function for each item
def delete_items(): 
    '''Deletes objects after their lifespan is over'''
    global items
    i=0
    while (i<len(items)): #For each item
        if (items[i].is_dead()): #If the item is dead
            del items[i] #delete item
            i-=1 #decrement index since deleted element
        i+=1 #increment index
def update(): #When needed, update screen
    '''Calls all necessary functions for each game frame'''
    create_item()
    update_items()
    delete_items()
    draw()
def on_press(key): 
    '''Key press event'''
    global sprite, canvas, canvas_x, canvas_y
    if(key==Key.left): #Left arrow key
        sprite.left()
        update()
    elif(key==Key.right): #Right arrow key
        sprite.right(canvas_x)
        update()
    elif(key==Key.up): #Up arrow key
        sprite.up()
        update()
    elif(key==Key.down): #Down arrow key
        sprite.down(canvas_y)
        update()
    else:
        try: #Check for character q, but pass if no character is found
            if(key.char==('q')):exit() #If q clicked, quit
        except AttributeError: pass
    
canvas_x=30 #Game width
canvas_y=15 #Game height
points=0 #Start with no points
#Print game instructions
print("\nINSTRUCTIONS:")
print("1. Create your character")
print("2. Move using arrow keys, q to quit")
print("3. Collect some items and avoid others")
print("4. Items despawn after a certain number\n   of moves, so move carefully")
print("5. However, watch for the time limit")
print("            Point guide:")
print("[+=1][-=-1][!=3][$=5][?=Random][Other=0-1]")
input("     Press enter to continue\n")
canvas=Mapper(canvas_x, canvas_y) #Create game canvas with Mapper using width and height defined
sprite=Character() #Main sprite is a character
items=[] #Empty array of game items to start
start_time = time.time() #Start time uses unix time
draw() #Draw first frame of game to begin
'''
The game only updates through keyboard events
On a given click, it runs a function to update the game
This way there is not wasted processing
Obviously the game could be a lot better, 
but I wanted to make it as "from scratch" as possible,
without using pygame or things like that.
I have noticed one bug where an item will break the wall,
but it happens so rarely I haven't been able to identify the
problem with debugging. 
I tried to incorporate all of the stuff we have done,
obviously with classes and objects, but also sorting lists,
etc. 
Hopefully this is enough to earn me a 100% in the course.
'''

with Listener(on_press=on_press) as listener: listener.join() #Code to keep checking for keyboard input