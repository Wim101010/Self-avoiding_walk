#this script draws differend kinds of path's
#the first function is deciding whihc path to draw based on your input
#the second function draws a completely random path
#the third function draws a non-reversing path
#the fourth function draws a self avoiding walk

import random
import turtle
import numpy as np

#decides which inputs to use and what type of path to draw
def draw(length, type):
    if type == "RAN": #this is the completely random path
        random_path(length)
    if type == "SAW": #self avoiding walk
        SAW(length)
    if type == "NRE": #non reversing path
        non_reverse(length)

def random_path(length):
    screen = turtle.getscreen() #open the drawing screen
    turtle.title("Random Path") 
    p = turtle.Turtle() #p is the "cursor"
    p.speed(100) #you can put this at whatever you want 

    position = (0,0) #starting point
    path = [] #not realy needed here to save the path but can be used to represent the path as a list instead of a drawing
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    for i in range(length):
        move = random.choice(movements)
        dx = move[0] #horizontal movement
        dy = move[1] #vertical movement

        position = (position[0]+dx,position[1]+dy) #new position
        p.goto(position) #move cursor
        path.append(position) 
    input("Press enter to continue") #otherwise the screen will dissapear when it's finished with drawing

def non_reverse(length): #works very similar to random path
    screen = turtle.getscreen()
    turtle.title("Non Reversing Path")
    p = turtle.Turtle()
    p.speed(100)

    position = (0,0)
    path = []
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    for i in range(length):
        if i > 0:
            backward = tuple(-1*np.array(move)) #this is the opposite of the last move
            movements.remove(backward) #we remove that move because it cant reverse

        move = random.choice(movements)
        dx = move[0]
        dy = move[1]

        position = (position[0]+dx,position[1]+dy)
        p.goto(position)
        #p.stamp() #this is a testfunction

        path.append(position)   
        if i>0:
            movements.append(backward) #we have to put it back into the possible moves otherwise it will run out of possible moves
    input("Press enter to continue ")

def SAW(length): #very similar to RAN and NRE
    screen = turtle.getscreen()
    turtle.title("Self-Avoiding Walk")
    p = turtle.Turtle()
    p.speed(100)

    position = (0,0)
    path = []
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    for i in range(length):
        movements = [(0,10),(10,0),(-10,0),(0,-10)]
        valid_move = False 
        while valid_move == False: #while loop to see possible moves
            move = random.choice(movements)
            dx = move[0]
            dy = move[1]
            new_position = (position[0]+dx,position[1]+dy)
            if new_position not in path: #if it wants to move to an empty lattice, do that move
                valid_move = True
            else: 
                movements.remove(move) #otherwise remove that move and try again
                if movements == []: #this happens when it is at a dead end
                    print("Dead end")
                    input("Press enter to continue ") 

        position = (position[0]+dx,position[1]+dy)
        p.goto(position)
        path.append(position)
  
    input("Press enter to continue ")

input1 = int(input("Give the lengt of the path you want to see as an integer: "))
input2 = input("Type RAN for a random path, SAW for a self-avoiding walk or NRE for a non-reversing path: ")

draw(input1, input2)