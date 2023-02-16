import sys
from typing import List


# class Path:
#     def __init__(self, path: List[int]):
#         self.root = [path]
#

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows_range = range(len(mat))
        cols_range = range(len(mat[0]))

        output = [[-1 for m in cols_range] for n in rows_range]
        queue = []

        all_ones = True
        for i in rows_range:
            for j in cols_range:
                if mat[i][j] == 0:
                    output[i][j] = 0
                    queue.append([i, j])
                    all_ones = False

        if all_ones:
            return [[0 for m in cols_range] for n in rows_range]

        while queue:
            row_index, col_index = queue.pop(0)
            distance = output[row_index][col_index]

            def visitCell(row: int, col: int) -> int:
                # if the cell not in the range - we skip it
                if row not in rows_range or col not in cols_range:
                    return 0
                # we visited this cell
                if output[row][col] >= 0:
                    return 0
                if output[row][col] < 0:
                    queue.append([row, col])
                    output[row][col] = distance + 1

            visitCell(row_index + 1, col_index)
            visitCell(row_index - 1, col_index)
            visitCell(row_index, col_index + 1)
            visitCell(row_index, col_index - 1)

        return output


solution = Solution()
# print(solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
# print(solution.updateMatrix([[1,1,0],[1,0,0],[0,0,0]]))
# print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(solution.updateMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 0]]))
