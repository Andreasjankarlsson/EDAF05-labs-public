import sys
import heapq

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connections = dict()
        self.visited = False

def main():
    lines_raw = sys.stdin.readlines()
    lines = []
    # Create nodes
    first_line =  lines_raw[0].strip().split()
    nbrNodes = int(first_line[0])
    node_list = list()
    for i in range(nbrNodes):
        node = Node(i+1)
        node_list.append(node)

    for i in range(1, len(lines_raw)):
        line_data =  lines_raw[i].strip().split()
        line_data = list(map(int, line_data))
        lines.extend(line_data)
        node_name1 = int(line_data[0])
        node_name2 = int(line_data[1])
        weight = int(line_data[2])

        # Connect
        node1 = node_list[node_name1-1]
        node1.connections[node_name2] = weight
        node2 = node_list[node_name2-1]
        node2.connections[node_name1] = weight
    Jarnik(node_list)

def Jarnik(node_list):
    heapqueue =[]
    T = set()
    start_node = node_list[0]
    start_node.visited = True
    T.add(start_node)
    for (key,value) in start_node.connections.items():
        heapq.heappush(heapqueue,(value,key)) 
    Q = dict()
    for node in node_list:
        Q[node.node_id] = node

    del Q[start_node.node_id]

    path_length=0
    
    while Q:
        shortest=99999999999999
        min_node_to = None
        while(True):
            # Pop the side with the smallest weight.
            heappop = heapq.heappop(heapqueue)
            next_node_index = heappop[1]
            next_node = node_list[next_node_index-1]         

            if not next_node.visited: #If we haven't been to that node, mark it as visited, 
                #add weight to our path, add all of this nodes connections to our heapList.
                next_node.visited = True
                path_length += heappop[0]
                for (key,value) in next_node.connections.items():
                    heapq.heappush(heapqueue,(value,key)) 
                T.add(next_node)            
                del Q[next_node.node_id]
                break
            
        
    print(path_length)



        

main()