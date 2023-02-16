from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums_length = len(nums)
        # if nums_length == 0:
        #     return 0
        #
        # start_index = 0
        # end_index = nums_length - 1
        # items_to_remove = 0
        # while start_index <= end_index:
        #     if nums[start_index] == val:
        #         while end_index >= start_index:
        #             items_to_remove += 1
        #             if nums[end_index] != val:
        #                 nums[start_index] = nums[end_index]
        #                 end_index -= 1
        #                 start_index += 1
        #                 break
        #             end_index -= 1
        #     else:
        #         start_index += 1
        #
        # return nums_length - items_to_remove

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

solution = Solution()
result = solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(result)
