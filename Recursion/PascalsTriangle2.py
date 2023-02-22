from typing import List


class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    #     if rowIndex == 0:
    #         return [1]
    #     if rowIndex == 1:
    #         return [1, 1]
    #
    #     result = [1, 1]
    #     for i in range(2, rowIndex + 1):
    #         prev = 1
    #         for j in range(1, i):
    #             temp = result[j]
    #             result[j] = prev + result[j]
    #             prev = temp
    #         result.append(1)
    #     return result
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
            row.append(1)
        return row


solution = Solution()
print(solution.getRow(3))
print(solution.getRow(4))
print(solution.getRow(5))
