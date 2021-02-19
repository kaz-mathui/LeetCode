class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                # print(i,j)
                if s[j:i+j] == s[j:i+j][::-1]:
                    return s[j:i+j]
# Runtime: 4884 ms, faster than 25.37% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.7 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.