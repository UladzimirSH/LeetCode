class Solution:
    def __init__(self):
        self.intermediate_results = {}

    def fib(self, n: int) -> int:
        if n in self.intermediate_results:
            return self.intermediate_results[n]
        result = None
        if n < 2:
            result = n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)

        self.intermediate_results[n] = result
        return result
