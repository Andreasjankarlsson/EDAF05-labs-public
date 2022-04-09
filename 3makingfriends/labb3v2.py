import sys

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
    T = set()
    start_node = node_list[0]
    start_node.visited = True
    T.add(start_node)
    Q = node_list[0:]
    Q.remove(start_node)
    path_length=0
    while Q:
        shortest=99999999999999
        min_node_to = None
        for e in T:
            for key,value in e.connections.items():
                node = node_list[key-1]
                
                if value < shortest and node.visited==False:
                    shortest = value
                    min_node_to = node
        
        min_node_to.visited = True
        Q.remove(min_node_to)
        T.add(min_node_to)
        path_length += shortest
    print(path_length)



        

main()