class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # lists = []
        # ans = 0
        # for i in range(len(nums)):
        #     ans += nums[i]
        #     lists.append(ans)
        # return lists
        return itertools.accumulate(nums)