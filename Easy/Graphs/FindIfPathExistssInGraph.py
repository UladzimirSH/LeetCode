from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.neighbours = []


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Node):
        self.items.append(item)

    def pop(self) -> Node:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items


class Graph:
    nodes = {}

    def __init__(self, number_of_vertices):
        for i in range(number_of_vertices):
            new_node = Node(i)
            self.nodes[i] = new_node

    def add_edge(self, node1: int, node2: int):
        first_node = self.get_node(node1)
        second_node = self.get_node(node2)
        if second_node not in first_node.neighbours:
            first_node.neighbours.append(second_node)
            second_node.neighbours.append(first_node)

    def get_node(self, node: int) -> Node:
        return self.nodes[node]


class Solution:

    def __init__(self):
        self.stack = Stack()

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        if n == 0:
            return False

        graph = Graph(n)
        for edge in edges:
            graph.add_edge(edge[0], edge[1])

        source_node = graph.get_node(source)
        if not source_node.neighbours:
            return False

        self.stack.push(source_node)

        return self.search_path(self.stack, destination)

    def search_path(self, stack: Stack, destination: int) -> bool:
        while not stack.is_empty():
            node = stack.pop()
            if node.value == destination:
                return True
            node.visited = True
            for neighbour in node.neighbours:
                if neighbour.visited:
                    continue
                stack.push(neighbour)
        return False


solution = Solution()

print(solution.validPath(1, [], 0, 0))
print(True)
print("")

print(solution.validPath(3, [[0, 1]], 2, 1))
print(False)
print("")

print(solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(True)
print("")

print(solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print(False)
print("")

print(solution.validPath(11, [[0,1],[1,8],[1,7],[0,5],[5,9],[5,6],[6,4],[6,10],[4,3],[3,0]], 0, 10))
print(True)
print("")

print(solution.validPath(11, [[0,1],[1,8],[1,7],[0,5],[5,9],[5,6],[4,3],[3,0]], 0, 10))
print(False)
print("")
