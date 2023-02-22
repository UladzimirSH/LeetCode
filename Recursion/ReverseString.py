from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:

        def reverse_s(left: int, right: int):
            if left < right:
                s[left], s[right] = s[right], s[left]
                reverse_s(left + 1, right - 1)

        reverse_s(0, len(s) - 1)


solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s)
