# class Solution:
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     result = []
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if target == nums[i] + nums[j]:
#                 result.append(i)
#                 result.append(j)
#     return result
# def twoSum(self, nums: List[int], target: int) -> List[int]:
# hash_table = {}
# for i in range(len(nums)):
#     if nums[i] in hash_table:
#         return [hash_table[nums[i]], i]
#     else:
#         hash_table[target - nums[i]] = i


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # print(i, j)
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]


def main():
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
