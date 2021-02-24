class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        n -= 1
        # ans += alphabet[n%26]
        ans = alphabet[n%26] + ans
        n = n // 26
        while n >= 1:
            n -= 1
            ans = alphabet[n%26] + ans
            n = n // 26
            print(n)
        return ans
    
    
# class Solution:
#     def convertToTitle(self, n: int) -> str:
#         res = ""
#         while n > 0:
#             n -= 1  # 26 -> "Z"
#             res += chr(n % 26 + ord('A'))
#             n //= 26
#         return res[::-1]