# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         counts = [0]*101
#         for nn in nums:
#             counts[nn] += 1
        
#         return_counts = list()
#         for nn in nums:
#             if nn ==0:
#                 return_counts.append(0)
#             else:
#                 return_counts.append(sum(counts[:nn]))
#         return return_counts

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         lookup = {}
#         print(lookup)
#         print(sorted(nums))
#         for i, v in enumerate(sorted(nums)):
#             if v in lookup:
#                 continue
#             lookup[v] = i
#             print(lookup)
#         return [lookup[num] for num in nums]


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        return [sorted_nums.index(num) for num in nums]
