from typing import List


class Solution:
    @staticmethod
    def TwoSum(nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, n in enumerate(nums):
            if n in dictionary:
                return [dictionary[n], i]
            pair = target - nums[i]
            dictionary[pair] = i
        return []
