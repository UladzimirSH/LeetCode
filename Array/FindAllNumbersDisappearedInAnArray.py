from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        occurrences = [0] * len(nums)
        for n in nums:
            occurrences[n - 1] += 1

        result = []
        for i in range(len(occurrences)):
            if occurrences[i] == 0:
                result.append(i + 1)

        return result


solution = Solution()
arr = [4, 3, 2, 7, 8, 2, 3, 1]
#arr = [1, 1]
result = solution.findDisappearedNumbers(arr)
print(result)
