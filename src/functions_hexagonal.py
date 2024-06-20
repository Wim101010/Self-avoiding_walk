import numpy as np
import time
import math

#COUNT THE AMOUNT OF SAWS

#the arguments are:
#N = length of SAW
#n = the length we are formulating the paths of
#path = hash map with coordinates of the visited postions in order (none is placeholder)
#paths = list of paths
def count3nbr(N):
    start = time.time()
    paths = create_paths(N, N) 
    end = time.time()
    elapsed = end-start
    return (len(paths), elapsed)

def create_paths(N, n):
    paths=[]
    #We set the recursion base at n = 1 and fix the first step
    #By doing this you count only a quarter of the paths
    #Makes the calculation time faster
    if n == 0:
        path = {(0,0): None}#dictionairy with visited positions
        paths = [path]
        return paths
    
    for path in create_paths(N, n-1):
        i = list(path.items())[-1][0] #last postition
        if i[0] % 20 == 0: #to calculate the possible moves we have to know where this point is
            if i[1]%30 == 0: #we use 10, 5 since then the mod function is easy to use
                movements = [(0,10),(10,-5),(-10,-5)] 
            else:
                movements = [(0,-10),(10,5),(-10,5)]
        else:
            if (i[1]-15)%30 == 0: #same idea but y-axis is moved down 1,5 step
                movements = [(0,10),(10,-5),(-10,-5)]
            else:
                movements = [(0,-10),(10,5),(-10,5)]
        
        for move in movements: #now we itterate through all the possible moves
            new_position = (i[0]+move[0],i[1]+move[1])
            #if the position not previously visited, then append
            if new_position not in path: 
                #to decrease complexity of "in" we have used a dictionary for the path 
                taken_path = dict(path.copy())
                taken_path[new_position] = None
                paths.append(taken_path)
    return paths



#CALCULATE THE AVERAGE DISTANCE
def average_distance3nbr(N):
    start = time.time()
    paths = create_paths(N, N) 
    dis = []
    for path in paths:
        end = list(path.items())[-1][0] #last postition
        x = end[0]
        y = end[1]   
        dis.append(distance(x,y))   
    avg_distance = sum(dis)/len(dis)
    end = time.time()
    elapsed = end-start
    return (avg_distance, elapsed)

def distance(x,y):
    if y>=0:
        hor_steps=abs(int(x/10))
        ver_steps=(y+5)//15
        if  hor_steps>=ver_steps:
            return hor_steps+ver_steps
        else:
            if y%15==0:
                hor_steps=ver_steps
            else:
                hor_steps=ver_steps-1
            return hor_steps+ver_steps
    else:
        hor_steps=abs(int(x/10))
        ver_steps=(abs(y)//15)
        if hor_steps>=(ver_steps+1):
            return hor_steps+ver_steps
        else:
            if y%15==0:
                hor_steps=ver_steps
            else:
                hor_steps=ver_steps+1
            return hor_steps+ver_steps