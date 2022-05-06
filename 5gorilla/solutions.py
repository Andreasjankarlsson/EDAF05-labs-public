from calendar import c
from re import M
import sys
from operator import itemgetter

class charMap():
    cmap = dict()
    
class cMatrix():
    cmatrix = [[]]

class pMatrix():
    pmatrix =[[]]
    string1 = ""
    string2 = ""

class returnMatrix():
    returnmatrix = [[]]

def main():
    lines_raw = sys.stdin.readlines()

    #mapping characters to their id.
    characters  =  lines_raw[0].strip().split()
    char = dict()
    for i in range(0,len(characters)):
        char[characters[i]] = int(i)
    charMap.cmap = char

    #Setting up a matrix to figure out the value when two characters are matching.
    k = len(lines_raw[1].strip().split())
    connectionMatrix = [[0 for x in range(k)] for y in range(k)]
    for i in range(k):
        line = lines_raw[1+i].strip().split()
        for j in range(k):
            connectionMatrix[i][j] = int(line[j])
    cMatrix.cmatrix = connectionMatrix

    #Retrieving strings,
    Q = int(lines_raw[k+1].strip().split()[0])
    for i in range(k+2,k+2+Q):
        string1 = lines_raw[i].strip().split()[0]
        string2 = lines_raw[i].strip().split()[1]
        pMatrix.string1 = string1
        pMatrix.string2 = string2
        algorithm("","")
            

def algorithm(str1,str2):
    #Creating a "pointMatrix"
    matrix = [[0 for x in range(len(pMatrix.string1)+1)] for y in range(len(pMatrix.string2)+1)]
    returnMatrix.returnmatrix = [[0 for x in range(len(pMatrix.string1)+1)] for y in range(len(pMatrix.string2)+1)]


    for i in range(len(matrix[0])):
        matrix[0][i] = -4*i
        returnMatrix.returnmatrix[0][i]="left"
    for j in range(len(matrix)):
        matrix[j][0] = -4*j
        returnMatrix.returnmatrix[j][0]="top"
    pMatrix.pmatrix = matrix
    returnMatrix.returnmatrix[0][0]="done"

    #print(returnMatrix.returnmatrix)
    opt(len(pMatrix.string2),len(pMatrix.string1))
    #print(opt(len(pMatrix.string2),len(pMatrix.string1))) 
    #print(pMatrix.pmatrix)
    #print(returnMatrix.returnmatrix)
    #for i in range(len(returnMatrix.returnmatrix)):
    #    print(returnMatrix.returnmatrix[i])
    print(buildOutput())

def score(ci,cj):
    if ci=='*' or cj=='*':
        return -4
    
    c1 = charMap.cmap[ci]
    c2 = charMap.cmap[cj]
    return cMatrix.cmatrix[c1][c2]    

def opt(i,j):
    if i == 0:
        return j*-4
    if j == 0:
        return i *-4

    cj = pMatrix.string1[j-1] 
    ci = pMatrix.string2[i-1]

    diag = (score(ci,cj) + opt(i-1,j-1))
    top = -4 + opt(i-1,j)
    left = -4 + opt(i,j-1)
    best = max(diag,top,left)
    pMatrix.pmatrix[i][j] = best
    if pMatrix.pmatrix[i][j] == diag:
        returnMatrix.returnmatrix[i][j] = "diag"
    if pMatrix.pmatrix[i][j] == top:
        returnMatrix.returnmatrix[i][j] = "top"
    if pMatrix.pmatrix[i][j] == left:
        returnMatrix.returnmatrix[i][j] = "left"    
    return best
    
def buildOutput():
    col = len(returnMatrix.returnmatrix[0]) -1
    row = len(returnMatrix.returnmatrix) -1
    #print("row:"+str(row) +"    col:"+str(col))
    string1 = pMatrix.string1
    string2 = pMatrix.string2
    returnString1 =""
    returnString2 =""
    prev = ""
    while(True):
        current = returnMatrix.returnmatrix[row][col]
        if current == "done":
            return returnString1 +" " + returnString2
        elif prev == "diag":
            char1 = string1[col-1]
            char2 = string2[row-1]
            returnString1 = char1 + returnString1
            returnString2 = char2 + returnString2
            row -= 1
            col -= 1
        elif prev == "top":
            char1 = '*'
            char2 = string2[row-1]
            returnString1 = char1 + returnString1
            returnString2 = char2 + returnString2
            row -= 1
            col -= 0
        elif prev == "left":
            char1 = string1[col-1]
            char2 = '*'
            returnString1 = char1 + returnString1
            returnString2 = char2 + returnString2
            row -= 0
            col -= 1
        prev = current


    


        
main()
