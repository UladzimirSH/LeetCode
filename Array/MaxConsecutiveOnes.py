from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0
        for n in nums:
            if n == 0:
                if current_length > max_length:
                    max_length = current_length
                current_length = 0
            if n == 1:
                current_length = current_length + 1
        if current_length > max_length:
            max_length = current_length
        return max_length
