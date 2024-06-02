class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, "":10000}
        ans = 0
        before_char = ""
        for t in s:
            if romans[before_char] < romans[t]:
                ans += -2 * romans[before_char] + romans[t]
            else:
                ans += romans[t]
            before_char = t
        return ans
