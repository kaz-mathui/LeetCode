class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        cums = [nums[0]]
        for i in range(1, len(nums)):
            cums.append(cums[-1]+nums[i])
        if cums[-1] < s:
            return 0
        minimal_len = len(nums)
        for i in range(len(nums)):
            low, high = i, len(nums)-1
            while low <= high:
                mid = low + int((high-low)/2)
                sum_so_far = cums[mid]-cums[i] + nums[i]
                if sum_so_far >= s:
                    minimal_len = min(minimal_len, mid-i+1)
                    high = mid - 1
                else:
                    low = mid + 1
        return minimal_len