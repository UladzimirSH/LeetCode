from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_length = len(arr)
        if arr_length == 0:
            return

        temp_max = arr[arr_length - 1]
        for i in range(len(arr) - 1, -1, -1):
            possible_max = arr[i]
            arr[i] = temp_max
            if possible_max > temp_max:
                temp_max = possible_max

        arr[arr_length - 1] = -1

        return arr


solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
solution.replaceElements(arr)
print(arr)