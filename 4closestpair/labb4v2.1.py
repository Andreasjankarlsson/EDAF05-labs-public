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
    py_test1 = list()
    py_test2 = list()

    for pointY in py:
        if pointY in px[:breakIndex]:
            py_test1.append(pointY)
        if pointY in px[breakIndex:]:
            py_test2.append(pointY)

    dl = closestPair(px[:breakIndex], py_test1)
    dr = closestPair(px[breakIndex:], py_test2)
    d = min(dl,dr)

    #Combine,

    S = list()
    for y in py:
        if px[breakIndex].x-d<= y.x <= px[breakIndex].x+d:
            S.append(y)
    len_s = len(S)


    for i in range(len_s):
        for j in range(i+1, min(i + 11, len_s)):
            p, q = S[i], S[j]
            dst = distance(p, q)
            d = min(d,dst)    
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
        data_line = lines_raw[k].strip().split()
        x = int(data_line[0])
        y = int(data_line[1])

        p = [x,y] 
        Px.append(p)
        Py.append(p)
    Px = list(sorted(Px, key=attrgetter('x')))
    Py = list(sorted(Px, key=attrgetter('y')))
    print('%.6f' % closestPair(Px,Py))



    
    
        

main()
