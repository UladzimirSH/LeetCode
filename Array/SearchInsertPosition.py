from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        result = self.search(nums, [0, size - 1], target)

        if result == -1:
            return 0

        return result

    def search(self, nums: List[int], indexes, target: int) -> int:
        begin = indexes[0]
        end = indexes[1]

        if nums[begin] == target:
            return begin
        if nums[end] == target:
            return end
        if end - begin <= 1:
            if nums[end] < target:
                return end + 1
            elif nums[begin] < target:
                return begin + 1
            else:
                return begin - 1

        middle = (end + begin) // 2

        if nums[middle] >= target:
            return self.search(nums, [begin, middle], target)
        else:
            return self.search(nums, [middle, end], target)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 0))
