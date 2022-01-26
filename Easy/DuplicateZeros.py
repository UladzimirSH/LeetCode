from typing import List
from collections import deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        if len(arr) < 2:
            return
        temp = deque()
        i = 0
        while i < len(arr):
            if len(temp) != 0:
                temp.append(arr[i])
                left_value = temp.popleft()
                if left_value == 0:
                    arr[i] = left_value
                    if i + 1 != len(arr):
                        temp.append(arr[i + 1])
                        arr[i + 1] = 0
                        i += 2
                    else:
                        i += 1
                else:
                    arr[i] = left_value
                    i += 1
            elif arr[i] == 0:
                temp.append(arr[i + 1])
                arr[i + 1] = 0
                i += 2
            else:
                i += 1
        if i == len(arr):
            return
        if arr[i] != 0 and len(temp) != 0:
            arr[i] = temp.popleft()


solution = Solution()
example = [0, 0, 0, 0, 0, 0, 0]
solution.duplicateZeros(example)
print(example)
