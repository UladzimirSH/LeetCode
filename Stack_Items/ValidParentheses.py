class Solution:

    def isValid(self, s: str) -> bool:
        connected_brackets = {'(': ')', '{': '}', '[': ']'}

        if not s:
            return False

        stack = []

        for i in s:
            if i in connected_brackets:
                stack.append(connected_brackets[i])
            elif not stack or stack.pop() != i:
                return False

        return not stack


solution = Solution()
print(solution.isValid("{[]}"))
