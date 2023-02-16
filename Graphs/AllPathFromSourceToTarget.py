from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        destination = n - 1

        if n == 0:
            return []

        stack = []
        paths = []
        stack.append([0])

        while stack:
            path = stack.pop()
            # get last node
            neighbour_nodes = graph[path[-1]]
            if not neighbour_nodes:
                continue
            for node in neighbour_nodes:
                if node == destination:
                    final_path = path[:]
                    final_path.append(node)
                    paths.append(final_path)
                    continue
                new_path = path[:]
                new_path.append(node)
                stack.append(new_path)
        return paths


solution = Solution()
print(solution.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
