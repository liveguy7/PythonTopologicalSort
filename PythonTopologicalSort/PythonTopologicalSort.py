import sys
from tracemalloc import start

edges = {
    'a': ['c', 'b'],
    'b': ['d', 'e'],
    'c': [],
    'd': [],
    'e': []
    
    }

vertices = ['a','b','c','d','e']

def topologicalSort(start,visited,sort):
    current = start
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        if(neighbor not in visited):
            sort = topologicalSort(neighbor,visited,sort)
    sort.append(current)
    if(len(visited) != len(vertices)):
        for vertice in vertices:
            if vertice not in visited:
                sort = topologicalSort(vertice,visited,sort)

    return sort

sort = topologicalSort('a',[],[])
print(sort)


class Node():

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treeSort(arr):
    if(len(arr) == 0):
        return arr
    root = Node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    res = []
    return res





