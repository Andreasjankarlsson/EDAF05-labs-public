from operator import ne
import sys


#use python labb2.py < data/sample/1.in in terminal to start program.
def main():
    inputs = list(sys.stdin.read().replace('\n', ' ').split(' '))
    nbrWords = int(inputs[0])
    nbrQueries = int(inputs[1])
    nodeList = list()
    wordToNodeMap = dict()

    #For every word, make a node.
    for i in range(2,nbrWords+2):
        word = inputs[i]
        newNode = Node(word)
        nodeList.append(newNode)
        wordToNodeMap[word]=newNode

    #For everyNode, if the last 4 character in node1 exist in node2, connect node1 to node2.
    for i in range(0,len(nodeList)):
        currentNode = nodeList[i]
        word = nodeList[i].word
        #Make a set with 4 last characters.
        characters = list() #Remember to empty this one later.
        for j in range(len(word)-1,len(word)-5,-1):
            characters.append(word[j])
        #Check if word[k] contians char in characaters, if they do add
        for k in range(0,len(nodeList)):
            compareWord = str(nodeList[k].word)
            if k==i: # We don't want to make a connection to ourselves.
                pass
            else: #Se if checkedNodes word contains the characters.
                isConnected = False
                for c in characters: #Remove character from word if found, otherwise, break loop.
                    index = compareWord.find(c)
                    if index==-1:
                        isConnected = False
                        break
                    else:
                        compareWord = compareWord[:index] + compareWord[index+1:]
                        isConnected = True
                if isConnected: #If characters is empty -> all characters exists in listNode[k].word
                    currentNode.connectedTo.append(nodeList[k])
    #Now, we have a graph, it's time to check if you can go from nodex to nodeY.
    #Testing only first case.
    firstIndex = 2+nbrWords
    for i in range(0,nbrQueries):
        firstWord = inputs[firstIndex+2*i]
        secondWord = inputs[firstIndex+1+2*i]
        firstNode = wordToNodeMap[firstWord]
        print(BFS2(firstNode,secondWord))
        restoreNodes(nodeList)


def BFS2(node,word):
    steps=0
    layers = list()
    layers.insert(steps,list())

    node.visited = True
    layers[steps].append(node)
    if node.word == word: #If node.word is word -> return 0
        return steps
    while True: #Create a set with every step, if node.word == word, return step
        steps+=1
        layers.insert(steps,list())
        for n in layers[steps-1]: #for every node in prev layer-> add their neighbours to this layer
            for neigbour in n.connectedTo:
                if neigbour.word ==word:
                    return steps
                if not neigbour.visited:
                    layers[steps].append(neigbour)
                    neigbour.visited =True
        if not layers[steps]:
            return "Impossible"
     
def restoreNodes(nodeList):
    for node in nodeList:
        node.visited = False
"""
def BFS(node,word):
    visitedNodes = list()
    queue = list()
    steps = 0
    if(node.word == word):
        return steps
    visitedNodes.append(node)
    queue.append(node)
    while(queue):
        q = queue.pop(0)
        visitedNodes.append(q)
        steps +=1
        for neighbour in q.connectedTo:
            if neighbour not in visitedNodes:
                visitedNodes.append(neighbour)
                neighbour.cameFrom = q
                queue.append(neighbour)
            if neighbour.word == word:
                neighbour.cameFrom = q
                steps=0
                while neighbour is not node:
                    steps = steps+1
                    neighbour = neighbour.cameFrom
                return str(steps)
    return("Impossible")

"""
            
        


class Node:
    def __init__(self, word):
        self.word=word
        self.visited = False
        self.connectedTo = list()
        self.cameFrom =None

main()
