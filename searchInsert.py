# target in nums の部分：リスト内でターゲットを線形検索するため、計算量は O(n) です。
# nums.append(target) の部分：リストに要素を追加するため、計算量は O(1) です。
# nums.sort() の部分：リストをソートするため、計算量は O(n log n) です。
# nums.index(target) の部分：リスト内でターゲットを線形検索するため、計算量は O(n) です。
# 全体の計算量はソートの部分が支配的となり、最終的に O(n log n) となります。


# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)


# 二分探索のため、計算量は 𝑂(log𝑛) です。
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
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


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_searchInsert(self):
        test_cases = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),
            ([], 1, 0),
        ]

        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                print(f"Testing with nums={nums}, target={target}, expected={expected}")
                result = self.solution.searchInsert(nums, target)
                self.assertEqual(result, expected)
                print(f"Result: {result}")


if __name__ == "__main__":
    unittest.main()
