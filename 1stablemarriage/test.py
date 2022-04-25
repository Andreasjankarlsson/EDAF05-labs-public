import sys
inputs = list(sys.stdin.read().replace('\n', '').replace(' ',''))
nbrPairs = int(inputs[0])

for i in range(1,len(inputs)//(nbrPairs+1)+1): 
    lineData=[None]*(nbrPairs+1)
    if i==1:
        first=1
        last= first+nbrPairs+1
        lineData=inputs[first:last]
    else:
        first = (i-1)*nbrPairs +i
        last = first+nbrPairs+1
        lineData=inputs[first:last]

