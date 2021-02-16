# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         def backtrack(first = 0):
#             # if all integers are used up
#             if first == n:  
#                 output.append(nums[:])
#             for i in range(first, n):
#                 # place i-th integer first 
#                 # in the current permutation
#                 nums[first], nums[i] = nums[i], nums[first]
#                 # use next integers to complete the permutations
#                 backtrack(first + 1)
#                 # backtrack
#                 nums[first], nums[i] = nums[i], nums[first]
        
#         n = len(nums)
#         output = []
#         backtrack()
#         return output



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
# Runtime: 36 ms, faster than 87.99% of Python3 online submissions for Permutations.
# Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Permutations.