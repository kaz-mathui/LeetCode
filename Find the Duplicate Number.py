class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # low,high = nums[0],nums[nums[0]]
        # while low != high:
        #     print(low,high)
        #     low,high = nums[low],nums[nums[high]]
        #     print(low,high)
        # low = 0
        # print(low,high)
        # print('--------')
        # while low != high:
        #     print(low,high)
        #     low,high = nums[low],nums[high]
        #     print(low,high)
        # return low
        
        
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]