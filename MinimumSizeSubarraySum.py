class Solution(object):
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        curr_s = 0
        for right in range(len(nums)):
            curr_s += nums[right]
            while curr_s >= s:
                res = min(res, right - left + 1)
                curr_s -= nums[left]
                left += 1
                print(left,right,curr_s)
        return res if res != float('inf') else 0