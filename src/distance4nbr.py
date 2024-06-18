import numpy as np
import time
import math

def lattice(N): #this forms the lattice
    amount = (2*N+1)**2 #we increased the Lattice in size so that "moving over the edge" is not necessary
    cells = np.full(amount, True, dtype=bool)
    return cells

#the arguments are:
#N = length of SAW
#n = the length we are formulating the paths of
#latt = vector filled with Booleans wheter the path has passed this location
#i = location where the path has ended
#path = tuple(i, latt)
#paths = list of path

def distance_start(path, N):
    size = 2*N+1
    postion = path[0]
    start = 2*N**2+2*N
    hor_start = start%size
    ver_start = start//size
    hor_distance = postion%size - hor_start
    ver_distance = postion//size - ver_start
    distance = math.sqrt(hor_distance**2+ver_distance**2) #pythagors theorem
    return distance

def average_distance4nbr(N):
    start = time.time()
    #steps we want to take are:
    #do all possible steps we can take
    #add back
    paths = create_paths(N, N) 
    distance = []
    for path in paths:
        distance.append(distance_start(path, N))
    avg_distance = sum(distance)/len(distance)
    end = time.time()
    elapsed = end-start
    return (avg_distance, elapsed)

def create_paths(N, n):
    paths = []
    if n == 0:
        latt = lattice(N)
        latt[0]=False
        paths = [(2*N**2+2*N,latt)] #first element is starting posititon
        return paths
    
    movements = [1,-1, (2*N+1), -(2*N+1)] #change to nbr
    for path in create_paths(N, n-1):
        for move in movements: #nbr in nbrs
            latt = path[1]
            i = (path[0]+move)
            if latt[i]:
                latt_copy = list(latt.copy())
                latt_copy[i] = False
                paths.append((i, latt_copy))
    return paths

print(average_distance4nbr(4))
