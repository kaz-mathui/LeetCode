# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         afterS = ['']*len(s)
#         for i,j in enumerate(s):
#             print(i,j)
#             print(indices[i])
#             afterS[indices[i]] = j
#             print(afterS)
#         return ''.join(afterS)
            
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        print(sorted(zip(indices, s)))
        # return "".join(c for _, c in sorted(zip(indices, s)))
        return ''.join(j for i,j in sorted(zip(indices,s)))