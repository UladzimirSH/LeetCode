from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return image

        row_range = range(len(image))
        col_range = range(len(image[0]))
        initial_color = image[sr][sc]
        stack = []
        stack.append([sr, sc])

        while stack:
            cell_r, cell_c = stack.pop()
            # update the image color
            image[cell_r][cell_c] = color

            def visitCell(row_index: int, col_index: int):
                if row_index not in row_range \
                        or col_index not in col_range\
                        or image[row_index][col_index] == color\
                        or image[row_index][col_index] != initial_color:
                    return
                stack.append([row_index, col_index])

            visitCell(cell_r + 1, cell_c)
            visitCell(cell_r - 1, cell_c)
            visitCell(cell_r, cell_c + 1)
            visitCell(cell_r, cell_c - 1)

        return image


solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))