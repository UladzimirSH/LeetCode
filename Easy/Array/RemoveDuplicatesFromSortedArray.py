from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                continue
            else:
                nums[i] = nums[j]
                i += 1
        return i


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
