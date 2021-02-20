class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans,mod = 0,10**9+7
        nums.sort()
        for i,j in enumerate(nums):
            if target < j*2:
                break
            b = bisect.bisect(nums,target-j,lo=i)
            ans += pow(2, b-i-1, mod)
        return ans % mod
