import math
import numpy as np

def lattice(N): #this forms the lattice
    amount = (N+1)**2
    cells = np.full(amount, True, dtype=bool)
    return cells

#the arguments are:
#N = length of SAW
#n = the length we are formulating the paths of
#latt = vector filled with Booleans wheter the path has passed this location
#i = location where the path has ended
#path = tuple(i, latt)
#paths = list of path

def count(N):
    #steps we want to take are:
    #do all possible steps we can take
    #add back
    #when n == N count the amount of path's
    paths = create_paths(N, N)
    return len(paths)

def create_paths(N, n):
    paths = []
    if n == 0:
        latt = lattice(N)
        latt[0]=False
        paths = [(0,latt)]
        return paths
    
    movements = [1,-1, (N+1), -(N+1)] #change to nbr
    for path in create_paths(N, n-1):
        for move in movements: #nbr in nbrs
            latt = path[1]
            i = (path[0]+move)%len(latt)
            if latt[i]:
                latt_copy = list(latt.copy())
                latt_copy[i] = False
                paths.append((i, latt_copy))
    return paths

print(count(12))