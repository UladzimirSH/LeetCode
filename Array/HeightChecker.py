from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # we do counting sorting, because of range items in the heights
        counting = [0] * 100
        for n in heights:
            counting[n - 1] += 1

        for i in range(len(counting) - 1):
            counting[i + 1] += counting[i]

        expected = [0] * len(heights)

        for n in heights:
            index = counting[n - 1] - 1
            expected[index] = n
            counting[n - 1] -= 1

        counter = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                counter += 1
        return counter


solution = Solution()
arr = [1, 1, 4, 2, 1, 3]
result = solution.heightChecker(arr)
print(result)
