from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        capacity = max(weights)

        temp_days = 0
        stop_aggressive = False
        while capacity:
            weights_iterator = 0
            for i in range(days):
                temp_days += 1
                one_ship_capacity = 0
                while weights_iterator < len(weights) and weights[weights_iterator] <= capacity - one_ship_capacity:
                    one_ship_capacity += weights[weights_iterator]
                    weights_iterator += 1

            if temp_days == days and len(weights) == weights_iterator:
                return capacity

            temp_days = 0
            capacity += 1


solution = Solution()
print(solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3))
print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(solution.shipWithinDays([10,10,10,10,11,12,7,8,9,10], 5))
