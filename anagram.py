
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
#             タプルに文字列をソートしてから代入する
            ans[tuple(sorted(s))].append(s)
        print(ans)
        return ans.values()