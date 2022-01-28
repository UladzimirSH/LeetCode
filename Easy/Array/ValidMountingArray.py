from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        if arr[1] < arr[0]:
            return False

        increase = True
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if increase:
                if arr[i] < arr[i + 1]:
                    continue
                else:
                    increase = False
            else:
                if arr[i + 1] > arr[i]:
                    return False
        if increase:
            return False

        return True


solution = Solution()
result = solution.validMountainArray([0, 1, 2, 4, 2, 1])
print(result)
