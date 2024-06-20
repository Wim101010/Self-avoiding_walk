#this script draws a visualisation of a 3 neighbor's SAW by using turtle

import turtle
import random

movements = [False, (0,1),(0,-1)]
move = random.choice(movements)

def SAW(length): #very similar to RAN and NRE
    screen = turtle.getscreen()
    turtle.title("Self-Avoiding Walk")
    p = turtle.Turtle()
    p.speed(100)

    position = (0,0)
    path = []

    for i in range(length):
        movements = []  #either up or down
        if position[0] % 20 == 0:
            if position[1]%30 == 0:
                movements = [(0,10),(10,-5),(-10,-5)]
            else:
                movements = [(0,-10),(10,5),(-10,5)]
        else:
            if (position[1]-15)%30 == 0: #same idea but y-axis is moved down 1,5 step
                movements = [(0,10),(10,-5),(-10,-5)]
            else:
                movements = [(0,-10),(10,5),(-10,5)]
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

SAW(1000)