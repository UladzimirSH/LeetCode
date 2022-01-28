from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            length = len(str(n))
            if length % 2 == 0:
                count += 1
        return count
