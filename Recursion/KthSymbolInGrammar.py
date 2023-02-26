class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        row_length = 2 ** (n - 1)
        if k > row_length:
            return 1 if self.kthGrammar(n-1, k - row_length) == 0 else 0
        else:
            return self.kthGrammar(n-1, k)