class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        if K <= (2**(N-2)):
            return self.kthGrammar(N-1, K)
        return self.kthGrammar(N-1, K - 2**(N-2)) ^ 1
# class Solution(object):
#     def kthGrammar(self, N, K):
#         lastrow = '0'
#         while len(lastrow) < N:
#             lastrow = "".join('01' if x == '0' else '10'
#                               for x in lastrow)
#         return int(lastrow[-1][K-1])