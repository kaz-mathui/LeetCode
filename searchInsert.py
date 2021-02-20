# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # return bisect.bisect_left(nums,target)
        while left <= right:
            pivot = (left + right) // 2
            # print(pivot)
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left