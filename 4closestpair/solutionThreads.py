import sys
import math
from operator import attrgetter 
import concurrent.futures


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def distance(P1, P2):
    return math.sqrt((P2[0]-P1[0])**2 +(P2[1]-P1[1])**2)


def closestPair(px,py):
    n = len(px)
    breakIndex = int(n/2)
    py_test = list()
    #Base-case
    if n==2:
        return distance(px[0],px[1])
    if n==3:
        minDist = min( distance(px[0],px[1]), distance(px[0],px[2]), distance(px[1],px[2]))
        return minDist
    
    # divide and calculate distance
    mid = px[int(n/2)]

    nmbr = 0
    sizen = len(py)


    dl = closestPair(px[:breakIndex], py)
    dr = closestPair(px[breakIndex:], py)
    d = min(dl,dr)

    for ileft in range(breakIndex,-1,-1):
        if px[ileft][0]<=(mid[0]-d):
            break
        py_test.append(px[ileft])

    for iright in range(breakIndex+1,len(px)):
        if px[iright][0]>= mid[0]+d:
            break
        py_test.append(px[iright])
    

    py_test = list(sorted(py_test, key=lambda tup: tup[1]))
    #Combine,
    S = py_test
    len_s = len(S)
    for i in range(len_s):
        for j in range(i+1, min(i + 11, len_s)):
            p, q = S[i], S[j]
            dst = distance(p, q)
            d = min(d,dst)    
    return d
   

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
    Px = list(sorted(Px, key=lambda tup: tup[0]))
    Py = list(sorted(Px, key=lambda tup: tup[1]))

    d = 9999999999999
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mid = int(len(Px)/2)
        future1 = executor.submit(closestPair, Px[0:mid], Py)
        print("len1:"+str(len(Px[0:mid])))
        future2 = executor.submit(closestPair, Px[mid:], Py)
        print("len2:"+str(len(Px[mid:])))
        result1 = future1.result()
        result2 = future2.result()
        d= min(d, result1, result2)
        compareList = list()

        for ileft in range(mid,-1,-1):
            if Px[ileft][0]<=(Px[mid][0]-d):
                break
            compareList.append(Px[ileft])

        for iright in range(mid+1,len(Px)):
            if Px[iright][0]>= Px[mid][0]+d:
                break
            compareList.append(Px[iright])
        
        compareList = list(sorted(compareList, key=lambda tup: tup[1]))
        #Combine,
        S = compareList
        len_s = len(S)
        for i in range(len_s):
            for j in range(i+1, min(i + 11, len_s)):
                p, q = S[i], S[j]
                dst = distance(p, q)
                d = min(d,dst)    
        #print('%.6f' % d)
    """
    with cProfile.Profile() as pr: 
        closestPair(Px,Py)  
        #print('%.6f' % closestPair(Px,Py))
        
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    print("hej")
    """
    



    
    
        

main()
