from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        queue = []
        rows_range = range(len(grid))
        columns_range = range(len(grid[0]))

        count_of_islands = 0

        for i in rows_range:
            for j in columns_range:
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append([i, j])
                    count_of_islands += 1

                def visit_cell(row, col, visited_before_room):
                    if row not in rows_range or col not in columns_range:
                        return
                    if grid[row][col] == '1':
                        grid[row][col] = '0'
                        queue.append([row, col])

                # we mark all connected parts of island as visited
                while queue:
                    # get cell and its indexes
                    cell = queue.pop(0)
                    row_index = cell[0]
                    col_index = cell[1]
                    # visit the cell above
                    visit_cell(row_index + 1, col_index, cell)
                    # visit the cell below
                    visit_cell(row_index - 1, col_index, cell)
                    # visit the cell from left
                    visit_cell(row_index, col_index - 1, cell)
                    # visit the cell from right
                    visit_cell(row_index, col_index + 1, cell)

        return count_of_islands


solution = Solution()
grid_test = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid_test))
