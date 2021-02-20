# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ans = 0
#         if not s:
#             return ans
#         for i in range(len(s)+1):
#             # ans += 1 
#             for j in range(i,len(s)+1):
#                 if self.is_palindrom(s[i:j]) and s[i:j]:
#                     # print(i,j,s[i:j])
#                     ans += 1
#         return ans

#     def is_palindrom(self, s):
#         return s == s[::-1]


class Solution:
    def countSubstrings(self, s: str) -> int:
        L, r = len(s), 0
        for i in range(L):
            for a,b in [(i,i),(i,i+1)]:
                print(a,b)
                while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
                r += (b-a)//2
        return r
