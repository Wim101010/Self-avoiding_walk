import random
import turtle

#class lattice:
    #def __init__(self, cells, lenght_SAW):
        

def path(length, type):
    if type == "Random":
        random_path(length)

def random_path(lenght):
    path = []
    screen = turtle.getscreen()
    turtle.title("Random Path")
    p = turtle.Turtle()
    p.speed(1000)
    for i in range(lenght):
        direction = random.randint(1, 4)
        if direction == 1:
            p.forward(10)
        if direction == 2:
            p.backward(10)
        if direction == 3:
            p.right(90)
            p.forward(10)
        if direction == 4:    
            p.left(90)
            p.forward(10)
    input("Press enter to continue")

random_path(1000)