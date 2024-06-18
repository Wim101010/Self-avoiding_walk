import numpy as np
import time

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

def count4nbr(N):
    start = time.time()
    #steps we want to take are:
    #do all possible steps we can take
    #add back
    #when n == N count the amount of path's
    paths = create_paths(N, N) 
    end = time.time()
    elapsed = end-start
    return (4*len(paths), elapsed) #times 4 to compensate for the symmetry

def create_paths(N, n):
    paths = []
    #We set the recursion base at n = 1 and fix the first step
    #By doing this you count only a quarter of the paths
    #Makes the calculation time faster
    if n == 1:
        latt = lattice(N)
        latt[0]=False
        latt[1]=False
        paths = [(1,latt)]
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
