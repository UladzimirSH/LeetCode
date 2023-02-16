from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        stack = [0]

        while stack:
            visited_room = stack.pop()
            # we visit room
            visited[visited_room] = 1
            # iterate through the next rooms we can visit and have keys
            for next_room in rooms[visited_room]:
                # if we did not visit this room before
                if visited[next_room] == 0:
                    stack.append(next_room)

        #if we have at least one unvisited room
        for i in visited:
            if i == 0:
                return False

        return True


solution = Solution()
print(solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))