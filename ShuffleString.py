class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        afterS = ['']*len(s)
        for i,j in enumerate(s):
            print(i,j)
            print(indices[i])
            afterS[indices[i]] = j
            print(afterS)
        return ''.join(afterS)
            