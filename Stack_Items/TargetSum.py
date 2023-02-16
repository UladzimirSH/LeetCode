from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        new_array = {target: 1}

        for n in nums:
            array = new_array
            new_array = {}
            while array:
                current_number = array.popitem()
                increase_number = current_number[0] + n
                decrease_number = current_number[0] - n

                if increase_number in new_array:
                    new_array[increase_number] = new_array[increase_number] + current_number[1]

                if decrease_number in new_array:
                    new_array[decrease_number] = new_array[decrease_number] + current_number[1]

                if increase_number not in new_array:
                    new_array[increase_number] = current_number[1]

                if decrease_number not in new_array:
                    new_array[decrease_number] = current_number[1]

                if decrease_number == increase_number:
                    new_array[decrease_number] = new_array[decrease_number] + current_number[1]

        if 0 in new_array:
            return new_array[0]

        return 0


solution = Solution()
print(solution.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)) #356
print(solution.findTargetSumWays([1, 0], 1))
print(solution.findTargetSumWays([1], 2))
print(solution.findTargetSumWays([1,1,1,1,1], 3))
print(solution.findTargetSumWays([35,42,34,22,35,39,35,44,33,48,46,18,4,39,1,50,28,43,15,37], 36))