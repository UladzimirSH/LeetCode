from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1


solution = Solution()
#arr = [0, 1, 0, 3, 12]
#arr = [0, 0, 0, 0]
arr = [0, 0, 0, 1]
solution.moveZeroes(arr)
print(arr)
