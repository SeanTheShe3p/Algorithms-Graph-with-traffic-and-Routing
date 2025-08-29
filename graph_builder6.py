def add_node():
    for row in weighted_array:
        row.append(0)
    new_row = [0 for i in range(len(weighted_array) + 1)]
    weighted_array.append(new_row)


def add_edge(start, destination, weight):
    weighted_array[start][destination] = weight


def remove_node(node):
    for rows in weighted_array:
        if rows[node] != 0:
            rows[node] = 0
    weighted_array.pop(node)
    
    
def remove_edge(start, destination):
    weighted_array[start][destination] = 0


def to_adjacency_list():
    i, j = 0 , 0
    fin = [("city"+str(i)+":") for i in range(len(weighted_array) - 1)]
    first = True
    for rows in weighted_array:
        j = 0  
        for cols in rows:
            if cols != 0:
                if first == True:
                    fin[i] += " city" + str(j) + "(" + str(cols) + ")"
                    first = False
                else:
                    fin[i] += ", city" + str(j) + "(" + str(cols) + ")"
            j += 1
        first = True
        i += 1
    for routes in fin:
        print(routes)


start, destination = (100, 100)
weighted_array = [[ 0 for i in range(start+1)] for j in range(destination+1)]

with open("input1.txt", "rt") as textFile:
    lines = textFile.readlines()
    for node in lines [1:11]:
        for edge in lines [102:]:
            if node.strip('\n') == edge [:6].strip(' '):

                
                start = int(node.strip('\n')[4:6])
                m = edge[10:].replace('\n','').split()
                destination = int(m[0])
                w = int(m[1])
                weighted_array[start][destination] += w

    for node in lines[11:101]:
        for edge in lines[102:]:
            if node.strip('\n') == edge [:7].strip(' '):

                start = int(node.strip('\n')[4:7])
                m = edge[11:].replace('\n','').split()
                destination = int(m[0])
                w = int(m[1])
                weighted_array[start][destination] += w
