import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s,len_p,set_p,ans = len(s),len(p),Counter(p),[]
        print(set_p)
        for i in range(len_s-len_p+1):
            if Counter(s[i:i+len_p]) == set_p:
                ans.append(i)
        return ans
