from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        copy_arr = [0] * len(nums)

        star_pointer = 0
        end_pointer = len(nums) - 1
        for n in nums:
            if n % 2 != 0:
                copy_arr[end_pointer] = n
                end_pointer -= 1
            else:
                copy_arr[star_pointer] = n
                star_pointer += 1
        return copy_arr


solution = Solution()
arr = [4, 5, 12, 7]
#arr = [0]
result = solution.sortArrayByParity(arr)
print(result)