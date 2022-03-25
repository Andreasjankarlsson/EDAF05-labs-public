import sys

def main():
    inputs = list(sys.stdin.read().replace('\n', ' ').split(' '))
    nbrPairs = int(inputs[0])
    
    #Datastructures
    wom_pref = dict()
    men_pref = dict()
    pairs = dict()
    singleMen = list() #SingleMen will be used as a FIFO-queue, as a "waitingline", where only the first is allowed to propose.

    #Converting input from .in file to datastructures
    for i in range(1,len(inputs)//(nbrPairs+1)+1): #Converting a long input-string to nbr+1 vectors.
        lineData=[None]*(nbrPairs+1)
        first = (i-1)*nbrPairs +i #Draw this and it will be quite straight-forward.
        last = first+nbrPairs+1
        lineData=inputs[first:last]
        lineData = list(map(int, lineData))
        data = lineData[:]

        #add these nbr+1 vectors as preferenses for person i.
        if not lineData[0] in wom_pref:
            pref = [None]*(nbrPairs+1)
            #wom_pref[person], will return the number of prioritisation.
            for j in range(1,nbrPairs+1):
                pref[data[j]]=j
            wom_pref[lineData[0]] = pref
            pairs[lineData[0]]=None
        else:
            men_pref[lineData[0]] = data[1:]
            singleMen.append(lineData[0])

    #Sorting algoritm, removes singleMan from queue.
    while singleMen:
        man = singleMen.pop()
        proposeTo = men_pref[man].pop(0)
        #If women doesn not have a partner, they will createa a pair
        if pairs[proposeTo] is None:
            pairs[proposeTo]=man
        #If woman get's proposed by a better partner, she will accept him, and the new single will be added to the list.
        elif wom_pref[proposeTo][man]<wom_pref[proposeTo][pairs[proposeTo]]:
            singleMen.append(pairs[proposeTo])
            pairs[proposeTo] = man
            
        #third case, man gets rejected 
        else :
            singleMen.append(man)

    #Print the result
    for i in range(1,nbrPairs+1):
        print((pairs[i]))
        
    

main()