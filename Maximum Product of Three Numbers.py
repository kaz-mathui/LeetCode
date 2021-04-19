class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        leng = len(nums)
        ans = max(nums[0]*nums[1]*nums[leng-1],nums[leng-1]*nums[leng-2]*nums[leng-3])
        return ans