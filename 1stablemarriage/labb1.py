
textFile = open("1stablemarriage/data/sample/1.in", 'r')
lines = textFile.readlines()
nbrPairs = int (lines[0])

men_pref = dict()
wom_pref = dict()

count=1
for i in range(1,len(lines)):
    lineData =  lines[i].strip().split()
    lineData = list(map(int, lineData))
    print(lineData)
    print(count)
    count += 1


