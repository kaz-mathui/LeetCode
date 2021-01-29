class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     result = []
    #     for i in range(len(nums)-1):
    #         for j in range(i+1,len(nums)):
    #             if target == nums[i] + nums[j]:
    #                 result.append(i)
    #                 result.append(j)
    #     return result
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        if nums[i] in hash_table:
            return [hash_table[nums[i]], i]
        else:
            hash_table[target - nums[i]] = i