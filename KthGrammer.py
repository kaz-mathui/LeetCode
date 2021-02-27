class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: return 0
        half = 2**(N-2)
        if K <= half:
            return self.kthGrammar(N-1, K)
        else:
            return 1 if self.kthGrammar(N-1, K-half) == 0 else 0