class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        for i in nums:
            temp = currMax
            currMax = max(prevMax + i,currMax)
            prevMax = temp
        return currMax