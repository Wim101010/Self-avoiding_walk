import turtle
import random
import numpy as np 
from abc import ABC, abstractmethod
from calculate4nbr import *

def necsize(length, nbr): #necessary cells
    size = length**(nbr/2)
    return int(size)
    #explained in used math

def cells(amount):
    cells = np.full(amount, True, dtype=bool)
    return cells
    #this creates an array of Booleans True

class Lattice(ABC):
    def __init__(self, nbr, lSAW):
        #lSAW is lengt of SAW
        #nbr is amount of neighbors for the lattice
        self.lSAW = lSAW
        self.nbr = nbr
        self.amountcells = necsize(self.lSAW, nbr) #necsize is a function that gives the necessary amount of cells for a particular lenght of SAW
        self.cells = cells(self.amountcells) #array of Booleans for all the cells
    
    def draw(self): #we can draw the SAW for nbr = 3 or 4
        pass

    def calculate(self): #we want to calculate the total amount of SAW's 
        #this function is only defined on 4 neigbhors/square lattice
        pass

    def distance(self): #is distance from starting point
        pass
        
class FourNbr(Lattice): #subclass for 2 dimensional lattice
    def __init__(self, nbr=4, lSAW=0): 
        super().__init__(4, lSAW) #we set neighbors to always 4, lenght of SAW is still a variable
        self.lSAW = lSAW

    def draw(self):
        print("Im trying to draw")
        super().draw() #this overpowers the draw() function implemented in the abstract class

        screen = turtle.getscreen()
        turtle.title("Self-Avoiding Walk with 4 neighbors")
        p = turtle.Turtle()
        p.speed(100)

        position = (0,0)
        path = [(0,0)]

        for i in range(self.lSAW):
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
                        turtle.exitonclick()

            position = (position[0]+dx,position[1]+dy)
            p.goto(position)
            path.append(position)
            turtle.exitonclick()

    def calculate(self):
        print("Calculating...")
        output = count4nbr(self.lSAW)
        print("For lenght", self.lSAW, "there are", f'{output[0]:_}', "possible SAW's. \n Calculation time: ", format(output[1], '.3E'))

class ThreeNbr(Lattice):
    def __init__(self, nbr=3,lSAW=0):
        super().__init__(3, lSAW) #we set neighbors to always 3, lenght of SAW is still a variable

    def draw(self): #this function overpowers the abstract draw function 
        super().draw
        
        screen = turtle.getscreen()
        turtle.title("Self-Avoiding Walk with 3 neighbors")
        p = turtle.Turtle()
        p.speed(100)

        position = (0,0)
        path = [(0,0)]

        for i in range(self.lSAW):
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
                        turtle.exitonclick()

            position = (position[0]+dx,position[1]+dy)
            p.goto(position)
            path.append(position)
        turtle.exitonclick()

testcase = FourNbr(lSAW=13)
testcase.calculate()