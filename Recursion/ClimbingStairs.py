class Solution:
    def __init__(self):
        self.intermediate_results = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0

        left_result = None
        if n - 1 in self.intermediate_results:
            left_result = self.intermediate_results[n - 1]
        else:
            left_result = self.climbStairs(n - 1)
            self.intermediate_results[n - 1] = left_result

        right_result = None
        if n - 2 in self.intermediate_results:
            right_result = self.intermediate_results[n - 2]
        else:
            right_result = self.climbStairs(n - 2)
            self.intermediate_results[n - 2] = right_result
        return left_result + right_result


solution = Solution()
print(solution.climbStairs(38))
