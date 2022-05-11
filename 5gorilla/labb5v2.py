import sys
import numpy as np


class Score:
    charMap = dict()
    matchMatrix = [[]]

    def calcScore(crow,ccol):
        id_crow = Score.charMap[crow]
        id_ccol = Score.charMap[ccol]
        return Score.matchMatrix[id_crow][id_ccol]
#@profile
def main():
    lines_raw = sys.stdin.readlines()
    charMap = dict()

    #mapping characters to their id, charMap.
    characters  =  lines_raw[0].strip().split()
    for i in range(0,len(characters)):
        charMap[characters[i]] = int(i)
    Score.charMap = charMap

    #Setting up a matrix to figure out the value when two characters are matching.
    k = len(lines_raw[1].strip().split())
    matchMatrix = [[0 for x in range(k)] for y in range(k)]
    for i in range(k):
        line = lines_raw[1+i].strip().split()
        for j in range(k):
            matchMatrix[i][j] = int(line[j])
    Score.matchMatrix = matchMatrix


    #Retrieving strings, Q = nbr of strings
    Q = int(lines_raw[k+1].strip().split()[0])
    for i in range(k+2,k+2+Q):
        string1 = lines_raw[i].strip().split()[0]
        string2 = lines_raw[i].strip().split()[1]
        tracebackTable, pointTable = buildTables(string1,string2)
        tracebackTabe = setTables(string1,string2,pointTable,tracebackTable)
        returnString1, returnString2 = returnStrings(string1,string2,tracebackTable)
        print(returnString1 +" " +returnString2)

#@profile       
def returnStrings(string1,string2,tracebackTable):
    row = len(tracebackTable) -1
    col = len(tracebackTable[0])-1
    returnString1 = ""
    returnString2 = ""
    while(True):
        if tracebackTable[row][col] == "d":
            returnString1 = string1[col-1] + returnString1
            returnString2 = string2[row-1] + returnString2
            row -= 1
            col -= 1
        elif tracebackTable[row][col] == "l":
            returnString1 = string1[col-1] + returnString1
            returnString2 = '*'+ returnString2
            col -= 1

        elif tracebackTable[row][col] == "t":
            returnString1 = '*' + returnString1
            returnString2 = string2[row-1]+ returnString2
            row -= 1
        
        elif tracebackTable[row][col] == "f":
            break
    return returnString1,returnString2

#@profile
def setTables(string1,string2,pointTable, tracebackTable):
    for row in range(1,len(string2)+1):
        for col in range(1,len(string1)+1):
            ccol = string1[col-1]
            crow = string2[row-1]
            diag = Score.calcScore(crow,ccol) + pointTable[row-1][col-1]
            left = (-4) + pointTable[row][col-1]
            top = (-4) + pointTable[row-1][col]
            pointTable[row][col] = max(diag,left,top)
            if pointTable[row][col] == diag:
                tracebackTable[row][col] = "d"
            elif (pointTable[row][col]) == left:
                tracebackTable[row][col] = "l"
            else:
                tracebackTable[row][col] = "t"
    return tracebackTable

#@profile
def buildTables(string1,string2):
    col = len(string1)
    row = len(string2)
    pointTable = np.zeros(shape=(row+1,col+1))
    tracebackTable = np.zeros(shape=(row+1,col+1),dtype=str)

    for i in range(col+1):
        pointTable[0][i] = i * -4
        tracebackTable[0][i] = "l"

    for j in range(row+1):
        pointTable[j][0] = j * -4
        tracebackTable[j][0] = "t"
    
    tracebackTable[0][0] = "f"
    return tracebackTable, pointTable


main()