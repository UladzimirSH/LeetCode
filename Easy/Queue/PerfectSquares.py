class Solution:
    def numSquares(self, n: int) -> int:
        visited = [0] * n
        queue = set()

        perfect_squares = self._get_all_perfect_squares(n)
        if not perfect_squares:
            return 0

        queue.append([n, 0])

        while queue:
            # get number from queue
            current_result, turn = queue.pop(0)
            turn += 1
            # for each number subtract all possible perfect_squares
            for p in perfect_squares:
                new_result = current_result - p
                # we found result
                if new_result == 0:
                    return turn
                # there is no reason to check the already checked numbers
                if new_result < 0 or visited[new_result] == 1:
                    continue
                queue.append([new_result, turn])
                visited[new_result] = 1
        return -1

    def _get_all_perfect_squares(self, n: int) -> []:
        perfect_squares = []
        i = 1
        while i * i <= n:
            perfect_squares.append(i * i)
            i += 1
        return perfect_squares


solution = Solution()
print(solution.numSquares(1))
