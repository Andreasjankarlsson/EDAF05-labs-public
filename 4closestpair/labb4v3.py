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
    breakIndex = int(n/2)
    #Base-case
    if n==2:
        return distance(px[0],px[1])
    if n==3:
        minDist = min( distance(px[0],px[1]), distance(px[0],px[2]), distance(px[1],px[2]))
        return minDist
    
    # divide and calculate distance
    mid = px[int(n/2)]
    dl = closestPair(px[:breakIndex], py)
    dr = closestPair(px[breakIndex:], py)
    d = min(dl,dr)

    #Combine,

    S = list()
    for y in py:
        if px[breakIndex].x-d<= y.x <= px[breakIndex].x+d:
            S.append(y)

    best = d  # assign best value to delta
    ln_y = len(S)  # store length of subarray for quickness

    ##Only examines points of left side/on line.
    for i in range(ln_y - 1):
        if S[i].x<=px[breakIndex].x:
            for j in range(i+1, ln_y):
                if S[j].y >= px[breakIndex].y+d:
                    break
                if S[j].x >= px[breakIndex].x+d:
                    break
                
                p, q = S[i], S[j]
                d2 = distance(p,q)
                d = min(d,d2)
            for j in range(i-1, 0, -1):
                if S[j].y >= px[breakIndex].y+d:
                    break
                if S[j].x >= px[breakIndex].x+d:
                    break
                p, q = S[i], S[j]
                d2 = distance(p,q)
                d = min(d,d2)
     
    return d
    """
    for p in py:
        if mid.x-d < p.x < mid.x+d :
            S.append(p)
    """
    """
    #Check points thats "between" two blocks.
    for i in range(0,len(S)):
        s = S[i]
        centerX = px[breakIndex].x
        centerY = px[breakIndex].y
        if True:
            for index in range(i+1,len(S)):             
                if S[index].y >= centerY+d:
                    break
                if S[index].x >= centerY+d:
                    break
                d2 = distance(S[index],s)
                d = min(d,d2)
            for index in range(i,0,-1):
                if s!=S[index]:
                    if S[index].y >= centerY+d:
                        break
                    if S[index].x >= centerY+d:
                        break
                    d2 = distance(S[index],s)
                    d = min(d,d2)
            
    return d
    """
    

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
