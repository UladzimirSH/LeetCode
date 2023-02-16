class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""

        stack = []
        for i in s:
            if i == "[":
                stack.append(i)
                continue

            if i == "]":
                str = ""
                while not stack[-1].isdigit():
                    str_part = stack.pop()
                    # if equal then we read all string and ready to multiply it
                    if str_part != "[":
                        str = str_part + str
                repeat_number = int(stack.pop())
                repeated_str = str * repeat_number
                stack.append(repeated_str)
                continue

            if i.isdigit():
                if stack and stack[-1].isdigit():
                    stack.append(stack.pop() + i)
                else:
                    stack.append(i)
                continue

            if stack and not stack[-1].isdigit() and stack[-1] != "[":
                stack.append(stack.pop() + i)
            else:
                stack.append(i)

        return ''.join(stack)


solution = Solution()
print(solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))