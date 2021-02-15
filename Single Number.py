# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
# #         hash_map = []
        
# #         for i in nums:
# #             if i in hash_map:
# #                 continue
# #             if i in nums:
# #                 hash_map.append(i)
# #             else:
# #                 return i

#         ans = 0
#         for n in nums:
#             ans ^= n
#         return ans

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()