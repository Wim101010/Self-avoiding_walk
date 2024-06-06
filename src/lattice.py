import turtle
import random
import numpy as np 
import pygame
from abc import ABC, abstractmethod

def necsize(length, nbr): #necessary cells
    size = length**2
    #see why this works in report

def cells(amount):
    cells = np.full(amount, True, dtype=bool)
    #this creates an array of Booleans True
    

class Lattice:
    def __init__(self, nbr, lSAW):
        #lSAW is lengt of SAW
        #nbr is amount of neighbors for the lattice
        self.lSAW = lSAW
        self.nbr = nbr
        self.amountcells = necsize(self.lSAW, nbr) #necsize is a function that gives the necessary amount of cells for a particular lenght of SAW
        self.cells = cells(self.amountcells) #array of Booleans for all the cells
    
    @abstractmethod
    def draw(self): #we can draw the SAW for nbr = 3 or 4
        pass

    #def calculate(self, nbr, lSAW): #we want to calculate the total amount of SAW's 
        
class Twodimensions(Lattice): #subclass for 2 dimensional lattice
    def __init__(self, nbr=4, lSAW=0): 
        super().__init__(4, lSAW) #we set neighbors to always 4, lenght of SAW is still a variable
        self.lSAW = lSAW

    def draw(self):
        screen = turtle.getscreen()
        turtle.title("Self-Avoiding Walk")
        p = turtle.Turtle()
        p.speed(100)

        position = (0,0)
        path = []

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
                        input("Press enter to continue ") 

            position = (position[0]+dx,position[1]+dy)
            p.goto(position)
            path.append(position)
    
        input("Press enter to continue ")

class Honeycomb(Lattice):
    def __init__(self, lSAW):
        super().__init__(3, lSAW) #we set neighbors to always 3, lenght of SAW is still a variable


TwoD = Lattice(4, 30)
TwoD.draw()