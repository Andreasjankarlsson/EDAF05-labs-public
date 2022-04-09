from collections import deque
import heapq
import sys

def main():
    inputs = list(sys.stdin.read().replace('\n', ' ').split(' '))
    nbrNodes = int(inputs[0])
    nbrVertices = int(inputs[1])
    visitedNodes = set()
    allNodes =set()
    possbileEdges= set()
    heapQueue = []

    #Create nodes, with weighted-edges that connects them.
    for i in range(0,nbrVertices):
        print(inputs)
        firstIndex=2+(i*3)
        firstNode = node(int(inputs[firstIndex]))
        secondNode = node(int(inputs[firstIndex+1]))
        weight = int(inputs[firstIndex+2])
        allNodes.add(firstNode)
        allNodes.add(secondNode)
        connectedEdge = edge(firstNode,secondNode,weight)
        firstNode.edges.append(connectedEdge)
        secondNode.edges.append(connectedEdge)
    
    #Begin with first node.
    node1 = allNodes[0]
    visitedNodes=node1
    node1.isVisited=True
    for e in node1.edges:
        if e not in possbileEdges:
            possbileEdges.add(e)
            heapq.heappush(heapQueue,(e.weight,e))
    while allNodes:
        currentEdge = heap


        for n in allNodes:
            for e in n.edges:
                print(e.weight)
                heapq.heappush(edgeHeap,(e.weight,e))


    heapq.heappush(edgeHeap,(2,edge(1,2,2)))        
    print(edgeHeap)
    print(heapq.heappop(edgeHeap)[1].weight)

    ##Tree is done.

    #List T: VisitedNodes.
    #List




class edge:
    def __init__(self,node1,node2,weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __hash__(self):
        return self.weight
    def __eq__(self,other):
        for e in other:
            print(e)
        if self.node1==other.node1 and self.node2==other.node2:
            return True
        elif self.node1==other.node2 and self.node2==other.node1:
            return True
        else:
            return False

class node:
    def __init__(self, nodeId):
        self.nodeId = nodeId
        self.edges = deque()
        self.isVisited = False
    def __hash__(self):
        return self.nodeId
    def __eq__(self,other):
        if(self.nodeId == other.nodeId):
            return True
        else:
            return False

main()
