class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        print(*strs)
        for num in zip(*strs):
            print(num)
            if len(set(num)) == 1:
                ans += num[0] 
            else:
                return ans
        return ans
