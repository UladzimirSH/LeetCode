class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            if x > 0:
                return 1
            else:
                return -1

        if n < 0:
            x = 1 / x
            n = -n

        def in_pow(number, power):
            if power == 0:
                return 1.0
            half = in_pow(number, power // 2)
            if power % 2 == 0:
                return half * half
            else:
                return half * half * number

        return in_pow(x, n)


solution = Solution()
# print(solution.myPow(-2, 0))
print(solution.myPow(-2, -3))
# print(solution.myPow(-2, 2))
# print(solution.myPow(-2, 3))