from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0

        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: self.int_division(a,b)
        }
        stack = []

        for i in tokens:
            try:
                digit = int(i)
                stack.append(digit)
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                c = operations[i](a, b)
                stack.append(c)

        return stack.pop()

    def int_division(self, a, b):
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return -(abs(a) // abs(b))
        else:
            return abs(a) // abs(b)


solution = Solution()
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(solution.evalRPN(["4","-2","/","2","-3","-","-"]))
