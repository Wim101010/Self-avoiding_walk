import random
import turtle
import numpy as np

#class lattice:
    #def __init__(self, cells, lenght_SAW):
        

def draw(length, type):
    if type == "RAN":
        random_path(length)
    if type == "SAW":
        SAW(length)
    if type == "NRE":
        non_reverse(length)

def random_path(length):
    screen = turtle.getscreen()
    turtle.title("Random Path")
    p = turtle.Turtle()
    p.speed(1)

    position = (0,0)
    path = []
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    for i in range(length):
        move = random.choice(movements)
        dx = move[0]
        dy = move[1]

        position = (position[0]+dx,position[1]+dy)
        p.goto(position)
        p.stamp()
        path.append(position)
        
    input("Press enter to continue")

def non_reverse(length):
    screen = turtle.getscreen()
    turtle.title("Non Reversing Path")
    p = turtle.Turtle()
    p.speed(1)

    position = (0,0)
    path = []
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    move = random.choice(movements)
    for i in range(length):
        backward = tuple(-1*np.array(move))
        movements.remove(backward)

        move = random.choice(movements)
        dx = move[0]
        dy = move[1]

        position = (position[0]+dx,position[1]+dy)
        p.goto(position)
        #p.stamp()

        path.append(position)   
        movements.append(backward)
    input("Press enter to continue")

def SAW(length):
    screen = turtle.getscreen()
    turtle.title("Self-Avoiding Walk")
    p = turtle.Turtle()
    p.speed(1000)

    position = (0,0)
    path = []
    movements = [(0,10),(10,0),(-10,0),(0,-10)]

    for i in range(length):
        movements = [(0,10),(10,0),(-10,0),(0,-10)]
        valid_move = False
        while valid_move == False:
            move = random.choice(movements)
            dx = move[0]
            dy = move[1]
            new_position = (position[0]+dx,position[1]+dy)
            if new_position not in path:
                valid_move = True
            else: 
                movements.remove(move)
                if movements == []:
                    print("Dead end")
                    input("Press enter to continue ") 

        position = (position[0]+dx,position[1]+dy)
        p.goto(position)
        path.append(position)
  
    input("Press enter to continue ")

input1 = int(input("Give the lengt of the path you want to see as an integer: "))
input2 = input("Type RAN for a random path, SAW for a self-avoiding walk or NRE for a non-reversing path: ")

draw(input1, input2)