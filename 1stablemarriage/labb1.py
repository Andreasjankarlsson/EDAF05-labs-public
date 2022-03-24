
textFile = open("1stablemarriage/data/sample/1.in", 'r')
lines = textFile.readlines()
nbrPairs = int (lines[0])

wom_pref = dict()
men_pref = dict()
pairs = dict()
singleMen = list()

for i in range(1,len(lines)):
    lineData =  lines[i].strip().split()
    lineData = list(map(int, lineData))
    prefList = dict()
    for j in range(1, len(lineData[1:])):
        prefList[j] = j

    if not lineData[0] in wom_pref:
        wom_pref[lineData[0]]= prefList
    else:
        men_pref[lineData[0]]= prefList


