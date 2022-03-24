
textFile = open("1stablemarriage/data/sample/2.in", 'r')
lines = textFile.readlines()
nbrPairs = int (lines[0])

#Datastructures
wom_pref = dict()
men_pref = dict()
pairs = dict()
singleMen = list() #SingleMen will be used as a stack

#Converting datafiles from txt.file to datastructures
row = 0
for i in range(1,len(lines)):
    row += 1
    lineData =  lines[i].strip().split()
    lineData = list(map(int, lineData))
    data = lineData[1:]

    if not lineData[0] in wom_pref:
        pref = [None]*(nbrPairs+1)
        #wom_pref[person], will return the number of prioritisation.
        for j in range(nbrPairs):
            pref[data[j]]=j
        wom_pref[lineData[0]] = pref
        pairs[lineData[0]]=None
    else:
        men_pref[lineData[0]] = data
        singleMen.append(lineData[0])

#Creating the sorting algoritm
while singleMen:
    man = singleMen.pop()
    proposeTo = men_pref[man].pop(0)
    if isinstance(pairs[proposeTo], type(None)):
        pairs[proposeTo]=man

    elif wom_pref[man]<wom_pref[pairs[proposeTo]]:
        singleMen.append(pairs[proposeTo])
        pairs[proposeTo] = man

    else :
        singleMen.append(man)

#Print the result
for i in range(1,nbrPairs+1):
    print(str(pairs[i]))