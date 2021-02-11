# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         target = []
#         for i in range(len(index)):
#             target.insert(index[i],nums[i])
#         return target
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, v in zip(index, nums):
            res.insert(i, v)
        return res