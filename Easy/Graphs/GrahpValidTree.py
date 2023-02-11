from typing import List


class Solution:
    root = []
    rank = []

    def findRoot(self, x) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.findRoot(self.root[x])
        return self.root[x]

    def union(self, x, y) -> bool:
        root_of_x = self.findRoot(x)
        root_of_y = self.findRoot(y)
        if root_of_x != root_of_y:
            if self.rank[root_of_x] > self.rank[root_of_y]:
                self.root[root_of_y] = root_of_x
            elif self.rank[root_of_x] < self.rank[root_of_y]:
                self.root[root_of_x] = root_of_y
            else:
                self.rank[root_of_x] += 1
                self.root[root_of_y] = root_of_x
            return True
        #if both have the same parent, then we have a cycle
        else:
            return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        if not edges or n == 0:
            return False

        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for edge in edges:
            if not self.union(edge[0], edge[1]):
                return False

        current_root = -1
        for i in range(n):
            root = self.findRoot(i)
            if current_root == -1:
                current_root = root
            if current_root == root:
                continue
            # we have more than one root
            else:
                return False

        return True


solutionTest = Solution()
print(solutionTest.validTree(10, [[5,6],[0,2],[1,7],[5,9],[1,8],[3,4],[0,6],[0,7],[0,3],[8,9]]))
print(False)
print("")
print(solutionTest.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(True)
print("")
print(solutionTest.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(False)
print("")
print(solutionTest.validTree(8, [[0, 1], [0, 2], [0, 3], [2, 4], [4, 5], [4, 6], [2, 7]]))
print(True)
print("")
print(solutionTest.validTree(8, [[0, 1], [0, 2], [0, 3], [2, 4], [4, 5], [4, 6], [2, 7], [6, 7]]))
print(False)
print("")
print(solutionTest.validTree(4, [[0, 1], [2, 3]]))
print(False)
print("")
print(solutionTest.validTree(3, [[1, 0]]))
print(False)
print("")
print(solutionTest.validTree(3, [[1, 0], [2, 0]]))
print(True)
print(solutionTest.validTree(3, [[1, 0], [0, 2]]))
print(True)
