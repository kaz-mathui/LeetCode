class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = last = 0
        num = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != num[i]:
                start = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != num[i]:
                last = i
                break
        print(last-start)
        # if 0:
        #     print(2)
        return last - start + 1 if last - start else 0
