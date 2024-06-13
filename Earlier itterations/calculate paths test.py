#this function calculate's the total amount of SAW's where each point has 4 neighbors
import math
import numpy as np

def necsize(length): #necessary size of the lattice
    size = (length+1)**2 #the + 1 is the starting position
    return size
    #explained in used math

def cells(lenght):
    amount = necsize(lenght)
    cells = np.full(amount, True, dtype=bool)
    return cells

def form_paths(N, remaining_length, I):
    if N == remaining_length:

    paths = []
    for i in I:
        form_paths(N, remaining_length+1,I)

    end = I[0]
    return paths #paths is a list of tuples

def form_p(N, remaining_lengt, I):
    if N == remaining_lengt:
        return (N, N, (0, cells(N)))
    if remaining_lengt > 0:
        form_p(N, remaining_lengt+1, I)
        


def make_valid_moves(i):
    N = int(math.sqrt(len[i[1]])) #this has to be made better
    movement = (1, -1, N, -N) 
    possible_paths = []
    for move in movement:
        i[1] = cells
        if cells[i[0]+move]:
            cells[i[0]+move]=False
            possible_paths.append((i[0]+movement,cells))
    return possible_paths

def check(postion, lattice, length): #returns how many moves are possible from this position
    N = int(length)
    movement = (1, -1, N, -N)
    j = 0
    for i in movement:
        if lattice[postion + i]:
            j += 1
    return j

#we use a recursive method
#save paths as a tuple of the lattice and the last position
#then check for every tuple how many last steps are possible
def count(N): #N = length SAW
    if N == 1:
        return 4
    if N == 2:
        return 8
    cells = cells(N) #here we create the lattice

    k = N-1
    paths_k = form_paths(k, cells) #k := N-1
    #do times 8

print(count)

