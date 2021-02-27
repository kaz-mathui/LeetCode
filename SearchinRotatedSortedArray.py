class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            elif nums[mid] > target:
                if target > nums[i]:
                    j = mid-1
                else:
                    if nums[mid] >= nums[i]:
                        i = mid+1
                    else:
                        j = mid-1
            else:
                if target < nums[i]:
                    i = mid+1
                else:
                    if nums[mid] >= nums[i]:
                        i = mid+1
                    else:
                        j = mid-1
        if nums[i] == target:
            return i
        return -1