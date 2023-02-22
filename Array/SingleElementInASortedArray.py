from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left_index = 0
        right_index = len(nums) - 1
        while left_index != right_index:
            middle = (right_index + left_index) // 2
            if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
                return nums[middle]

            middle_is_even = middle % 2 == 0
            if middle_is_even:
                if nums[middle] == nums[middle + 1]:
                    left_index = middle
                else:
                    right_index = middle
            else:
                if nums[middle] == nums[middle - 1]:
                    left_index = middle + 1
                else:
                    right_index = middle - 1

        return nums[left_index]


solution = Solution()
# print(solution.singleNonDuplicate([2, 2, 3]))
print(solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(solution.singleNonDuplicate([3, 3, 7, 7, 10, 10, 11, 11, 12]))
print(solution.singleNonDuplicate([0, 3, 3, 7, 7, 10, 10, 11, 11, 12, 12]))
print(solution.singleNonDuplicate([0, 1, 1, 2, 2, 5, 5]))
