from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        @lru_cache(None)
        def calc(index,S):
            if index == 0:
                 return  int(nums[0] == S) + int(-nums[0] == S)
            return  calc(index-1, S - nums[index]) + calc(index-1, S + nums[index])

        return calc(len(nums)-1, S)