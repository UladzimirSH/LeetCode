from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        if len(temperatures) == 1:
            return [0]

        stack = []
        answers = [0] * len(temperatures)
        #stack contains [value, index in temperatures]
        stack.append([temperatures[0], 0])

        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                value, index = stack.pop()
                answers[index] = i - index
            stack.append([temperatures[i], i])

        return answers


# 74, 72, 71, 72, 75
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
