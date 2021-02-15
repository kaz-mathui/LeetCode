class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         hash_map = []
        
#         for i in nums:
#             if i in hash_map:
#                 continue
#             if i in nums:
#                 hash_map.append(i)
#             else:
#                 return i

        ans = 0
        for n in nums:
            ans ^= n
        return ans