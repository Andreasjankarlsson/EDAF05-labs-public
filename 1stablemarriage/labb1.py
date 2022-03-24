
textFile = open("1stablemarriage/data/secret/0testsmall.in", 'r')
lines = textFile.readlines()
nbrPairs = int (lines[0])

wom_pref = dict()
men_pref = dict()

count=1
for i in range(1,len(lines)):
    lineData =  lines[i].strip().split()
    lineData = list(map(int, lineData))
    prefList = lineData[1:]
    if not lineData[0] in wom_pref:
        wom_pref[lineData[0]]= prefList
    else:
        men_pref[lineData[0]]= prefList

print("Wom_pref")
for i in wom_pref:
    print('woman' + str(i))
    print(wom_pref[i])

print("man_pref")
for i in men_pref:
    print("man" + str(i))
    print(men_pref[i])
