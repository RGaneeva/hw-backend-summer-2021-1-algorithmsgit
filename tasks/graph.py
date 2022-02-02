from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return Node({repr(self.value)})

    __repr__ = __str__


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        stack, nodes = [graph._root], []   
        while stack:
            vertex = stack.pop()
            if vertex in nodes:
                continue
            nodes.append(vertex)
            for neighbor in vertex.outbound:
                stack.append(neighbor)

    def bfs(self):
        visited = []
        queue = []
        visited.append(graph._root)
        queue.append(graph._root)
    
        while queue:
            s = queue.pop(0) 

            for neighbor in s.outbound:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        
        return visited
