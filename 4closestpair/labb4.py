import sys
import math
from operator import attrgetter 


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def distance(P1, P2):
    return math.dist((P1.x, P2.x), (P1.y, P2.y))

def closestPair(px,py):
    n = len(px)
    #Base-case
    if n==2:
        return distance(px[0],px[1])
    if n==3:
        minDist = math.min( distance(px[0],px[1]), distance(px[0],px[2]), distance(px[1],px[2]))
        return minDist
    
    # divide and calculate distance
    mid = px[n/2]
    dl = closestPair(px[:n/2], py)
    dr = closestPair(px[n/2:], py)
    d = math.min(dl,dr)

    #Combine,
    S = set()
    for point in py:
        if mid.x-d<py.x<mid.x+d:
            S.add(py)

    for point_index in range(0,len(S)):
        if S[point_index].x<mid.x:

            for i in range(point_index+1,n): #Go up
                if(S[i].y>S[point_index].y+d):
                    break
                deltaD = distance(S[point_index],S[i])
                d = math.min(d,deltaD)
            for i in range(n/2-1,0,-1): #Go down
                if(S[i].y<point.y+d):
                    break
                deltaD = distance(point,S[i])
                d = math.min(d,deltaD)
    return d

    

def main():
    print(str(math.dist(1,5)))
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
    Py = list(sorted(Px, key=attrgetter('y')))

    closestPair(Px,Py)
    #Add points to px,py. sort these later using a smart algorithm.

    #


    
    
        

main()
