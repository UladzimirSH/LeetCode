from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        roi = {}
        for i in range(len(profits)):
            roi[i] = profits[i] - capital[i]

        roi = dict(sorted(roi.items(), key=lambda x: x[1], reverse=True))

        for i in range(k):
            for profits_index, max_profit in roi.items():
                required_capital
                return 1

        return 0


solution = Solution()
print(solution.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
