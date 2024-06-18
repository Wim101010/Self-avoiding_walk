import numpy as np
import time
import math

def latt_optimized(N): #this forms the lattice needed for calculation the total amount of possible SAW's
    amount = (N+1)**2 #we only make a quarter of the lattice to improve on memory
    cells = np.full(amount, True, dtype=bool)
    return cells #the lattice is a list of Booleans

def square_latt(N): #this forms the lattice needed to calculate the average distance
    amount = (2*N+1)**2 #we increased the Lattice in size so that "moving over the edge" is not necessary
    cells = np.full(amount, True, dtype=bool)
    return cells

#the arguments are:
#N = length of SAW
#n = the length we are formulating the paths of
#latt = array filled with Booleans. False means the path has passed this location
#i = new postion/postion last visited
#path = (i, latt)
#paths = list of path

#CODE NEEDED TO CALCULATE TOTAL AMOUNT OF SAWs
def count4nbr(N):
    start = time.time()
    paths = create_paths(N, N) #we start the recursion
    end = time.time()
    elapsed = end-start
    return (4*len(paths), elapsed) #times 4 to compensate for the symmetry

def create_paths(N, n):
    paths = []
    
    if n == 1:
        #We set the recursion base at n = 1 and fix the first step
        #By doing this you count only a quarter of the paths (these paths are symmetric)
        #Makes the calculation time faster
        latt = latt_optimized(N)
        latt[0]=False #mark the postions the path has passed
        latt[1]=False 
        paths = [(1,latt)] 
        return paths
    
    movements = [1,-1, (N+1), -(N+1)] #the first to movements are left/right, second two are up/down (move the index 1 row)
    for path in create_paths(N, n-1): #with n = 1 there is only 1 path
        for move in movements: #make all possible moves
            latt = path[1]
            i = (path[0]+move)%len(latt)
            if latt[i]: #if the path has not been there, the move is valid
                latt_copy = list(latt.copy()) #create a new lattice for this path
                latt_copy[i] = False #in this path you set the new position as valse
                paths.append((i, latt_copy))
    return paths



#CODE NEEDED TO CALCULATE AVERAGE DISTANCE
def average_distance4nbr(N):
    start = time.time()
    paths = create_paths(N, N) #here we start the recursion
    distance = [] #this list has all the distances for the different SAW's of lenght N
    for path in paths: 
        distance.append(distance_start(path, N))
    avg_distance = sum(distance)/len(distance)
    end = time.time()
    elapsed = end-start
    return (avg_distance, elapsed)

def distance_start(path, N):
    size = 2*N+1 #the lenght of 1 row
    postion = path[0]
    start = 2*N**2+2*N #this is the mid-point of the lattice as an index
    hor_start = start%size #x-position
    ver_start = start//size #y-position
    hor_distance = postion%size - hor_start #dx between start and end
    ver_distance = postion//size - ver_start #dy between start and end
    abs_distance = math.sqrt(hor_distance**2+ver_distance**2) #Pythagora's theorem to calculate total distance
    return (abs_distance)

def create_paths(N, n): #We use a similar recursion as before, only with a changed row-lenght
    paths = []
    if n == 0:
        latt = square_latt(N)
        latt[0]=False
        paths = [(2*N**2+2*N,latt)] #first element is starting position (centre of the lattice)
        return paths
    
    movements = [1,-1, (2*N+1), -(2*N+1)] 
    for path in create_paths(N, n-1):
        for move in movements: 
            latt = path[1]
            i = (path[0]+move)
            if latt[i]:
                latt_copy = list(latt.copy())
                latt_copy[i] = False
                paths.append((i, latt_copy))
    return paths
