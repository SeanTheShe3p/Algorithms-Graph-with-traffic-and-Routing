def add_node(node, graph):
    graph.append({node: ""})   

def add_edge(city1, city2, weight, graph):
    graph.append({city1:str(city2) + '(' + str(weight) + ')'}) 

def remove_node(node, graph):
    i = 0
    for route in graph:
        x = next(iter(route.keys()))
        if x == node:
            del graph[i]
        i += 1

def to_adjacency_list(graph):
    fin = list(range(0,100))
    for i in range(100):
        fin[i] = "city" + str(fin[i]) + ": "
    prev = 0
    for route in graph:
        x = next(iter(route.keys()))
        if x != prev:
            fin[x] = str(fin[x]) + " city" + route.get(x)
            prev += 1
        else:
            fin[x] = str(fin[x]) + ", city" + route.get(x)
    for i in fin:
        print(i)

weighted_graph = []





with open("input1.txt", "rt") as textFile:
    lines = textFile.readlines()
    for node in lines [1:11]:
        for edge in lines [102:]:
            if node.strip('\n') == edge [:6].strip(' '):
                weighted_graph.append({int(node.strip('\n')[4:6]):edge[10:].replace('\n',')').replace(" ", "(")})

    for node in lines[11:101]:
        for edge in lines[102:]:
            if node.strip('\n') == edge [:7].strip(' '):
                weighted_graph.append({int(node.strip('\n')[4:7]):edge [11:].replace('\n',')').replace(" ", "(")})
                

to_adjacency_list(weighted_graph)