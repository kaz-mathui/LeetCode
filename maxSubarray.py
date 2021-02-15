# # class Solution:
# #     def cross_sum(self, nums, left, right, p): 
# #             if left == right:
# #                 return nums[left]

# #             left_subsum = float('-inf')
# #             curr_sum = 0
# #             for i in range(p, left - 1, -1):
# #                 curr_sum += nums[i]
# #                 left_subsum = max(left_subsum, curr_sum)

# #             right_subsum = float('-inf')
# #             curr_sum = 0
# #             for i in range(p + 1, right + 1):
# #                 curr_sum += nums[i]
# #                 right_subsum = max(right_subsum, curr_sum)

# #             return left_subsum + right_subsum   
    
# #     def helper(self, nums, left, right): 
# #         if left == right:
# #             return nums[left]
        
# #         p = (left + right) // 2
            
# #         left_sum = self.helper(nums, left, p)
# #         right_sum = self.helper(nums, p + 1, right)
# #         cross_sum = self.cross_sum(nums, left, right, p)
        
# #         return max(left_sum, right_sum, cross_sum)
        
# #     def maxSubArray(self, nums: 'List[int]') -> 'int':
# #         return self.helper(nums, 0, len(nums) - 1)

# class Solution:
#     def maxSubArray(self, nums: 'List[int]') -> 'int':
#         n = len(nums)
#         curr_sum = max_sum = nums[0]

#         for i in range(1, n):
#             curr_sum = max(nums[i], curr_sum + nums[i])
#             max_sum = max(max_sum, curr_sum)
#             print('curr_sum:',curr_sum)
#             print('max_sum:',max_sum)
            
#         return max_sum

# class Solution:
#     def maxSubArray(self, nums: 'List[int]') -> 'int':
#         n = len(nums)
#         max_sum = nums[0]
#         for i in range(1, n):
#             if nums[i - 1] > 0:
#                 nums[i] += nums[i - 1] 
#             max_sum = max(nums[i], max_sum)
            
#         # print(nums)
#         return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        max_num = max(nums)
        for i in range(len(nums)):
            temp += nums[i]
#             少なくとも0以上にならなければそこから切り捨てて始めた方がいいと言うイメージ
            if temp >= 0:
                max_num = max(max_num,temp)
            else:
                temp = 0
        return max_num
# Runtime: 60 ms, faster than 93.50% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.5 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.