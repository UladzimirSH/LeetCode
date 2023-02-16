from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = set()
        for n in arr:
            if n * 2 in doubles or n / 2 in doubles:
                return True
            else:
                doubles.add(n)
        return False


solution = Solution()
result = solution.checkIfExist([7, 1, 14, 11])
print(result)
