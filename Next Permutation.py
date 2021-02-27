class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. get the start index of non-increasing sequence from tail
        # 2. swap
        # 3. sort the non-increasing
        if not nums: return nums
        l = len(nums)
        i, j = l - 2, l - 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        while j > i and nums[j] <= nums[i]:
            j -= 1
        print(i,j)
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])