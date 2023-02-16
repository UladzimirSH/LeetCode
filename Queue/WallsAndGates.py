from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if len(rooms) == 0:
            return

        # contains a massive[row, column, distance to door]
        queue = []
        rows_range = range(len(rooms))
        columns_range = range(len(rooms[0]))

        visited = [[0 for j in columns_range] for i in rows_range]

        for i in rows_range:
            for j in columns_range:
                room = rooms[i][j]
                if room == 0:
                    queue.append([i, j, 0])
                if room == 0 or room == -1:
                    visited[i][j] = 1

        def visit_room(row, col, visited_before_room):
            if row not in rows_range or col not in columns_range:
                return
            if visited[row][col] == 0:
                visited[row][col] = 1
                new_distance = visited_before_room[2] + 1
                rooms[row][col] = new_distance
                queue.append([row, col, new_distance])

        while queue:
            #get room and its indexes
            room = queue.pop(0)
            row_index = room[0]
            col_index = room[1]
            # visit the room above
            visit_room(row_index + 1, col_index, room)
            # visit the room below
            visit_room(row_index - 1, col_index, room)
            # visit the room from left
            visit_room(row_index, col_index - 1, room)
            # visit the room below
            visit_room(row_index, col_index + 1, room)


solution = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
solution.wallsAndGates(rooms)
print(rooms)