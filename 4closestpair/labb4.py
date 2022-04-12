import sys
import math
from operator import attrgetter 


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def distance(P1, P2):
    return math.sqrt((P2.x-P1.x)**2 +(P2.y-P1.y)**2)

def closestPair(px,py):
    n = len(px)
    #Base-case
    if n==2:
        return distance(px[0],px[1])
    if n==3:
        minDist = min( distance(px[0],px[1]), distance(px[0],px[2]), distance(px[1],px[2]))
        return minDist
    
    # divide and calculate distance
    mid = px[int(n/2)]
    dl = closestPair(px[:int(n/2)], py)
    dr = closestPair(px[int(n/2):], py)
    d = min(dl,dr)

    #Combine,
    """
    S = list()
    for point in py:
        if mid.x-d< point.x <mid.x+d:
            S.append(point)

    for point_index in range(0,len(S)):
        if S[point_index].x<mid.x:

            for i in range(point_index+1,n): #Go up
                if(S[i].y>S[point_index].y+d):
                    break
                deltaD = distance(S[point_index],S[i])
                d = min(d,deltaD)
            for i in range(int(n/2)-1,0,-1): #Go down
                if(S[i].y<point.y+d):
                    break
                deltaD = distance(point,S[i])
                d = min(d,deltaD)
    return d
    """

    S = list()
    for p in py:
        if  mid.x-d < p.x < mid.x+d :
            S.append(p)


    #Check nodes upwards in list.
    """
    for elementIndex in range(0,len(S)):
        if(True): #S[elementIndex].x<=mid.x): #Here we can add things so we can halve things...
            for i in range(elementIndex+1,len(S)): #Travel up list.
                if S[i].x>=S[elementIndex].x: #Only check objects on edge or right side.
                    if(elementIndex!= i):
                        if(S[i].y>=S[elementIndex].y+d):
                            break 
                        deltaD = distance(S[elementIndex],S[i] )
                        d = min(d,deltaD)
            for j in range(elementIndex-1,0,-1):
                if S[j].x>=S[elementIndex].x:
                    if(elementIndex!= j):
                        if(S[j].y<S[elementIndex].y-d):
                            break
                        deltaD = distance(S[elementIndex],S[j] )
                        d = min(d,deltaD)
    """
             
    """
    for i in range(len(S)):
        for j in range(len(S)):
            if i!=j:
                d = min(d, (distance(S[i], S[j])))
    """

    for i in range(len(S)):
        for j in range(min(i+11,len(S))):
            if i!=j:
                d = min(d, (distance(S[i], S[j])))
    
    
    return d

    

def main():
    lines_raw = sys.stdin.readlines()
    # Create nodes
    first_line =  lines_raw[0].strip().split()
    nbr_points = int(first_line[0])
    Px = list()
    Py = list()
    for k in range(1, nbr_points+1):
        x = int(lines_raw[k].strip().split()[0])
        y = int(lines_raw[k].strip().split()[1])

        p = Point(x,y)  
        Px.append(p)
        Py.append(p)

    Px = list(sorted(Px, key=attrgetter('x')))
    Py = list(sorted(Py, key=attrgetter('y')))

    print('%.6f' % closestPair(Px,Py))
    #Add points to px,py. sort these later using a smart algorithm.

    #


    
    
        

main()
