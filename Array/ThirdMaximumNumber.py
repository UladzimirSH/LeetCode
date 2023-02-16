from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxs = [float('-inf'), float('-inf'), float('-inf')]
        for i in range(len(nums)):
            if maxs[2] == nums[i] or maxs[1] == nums[i] or maxs[0] == nums[i]:
                continue
            if nums[i] > maxs[2]:
                if nums[i] > maxs[1]:
                    if nums[i] > maxs[0]:
                        maxs[2] = maxs[1]
                        maxs[1] = maxs[0]
                        maxs[0] = nums[i]
                        continue
                    maxs[2] = maxs[1]
                    maxs[1] = nums[i]
                    continue
                maxs[2] = nums[i]

        if maxs[2] == float('-inf'):
            return maxs[0]

        return maxs[2]


solution = Solution()
# arr = [1, 1, 4, 2, 1, 3, 5, 9]
# arr = [1, 2]
#arr = [2, 2, 3, 1]
arr = [1,2,-2147483648]
result = solution.thirdMax(arr)
print(result)
