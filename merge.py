from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        nums1とnums2を非減少順にマージし、結果をnums1に格納する。
        """
        # 最後のインデックスから開始
        i = m - 1
        j = n - 1
        k = m + n - 1

        # nums1 と nums2 を後ろから比較しながらマージ
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2に残っている要素があればnums1にコピー
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# 計算量の詳細な説明：
# このアルゴリズムはnums1とnums2の両方を後ろから比較しながらマージするため、各要素について一度だけ処理を行います。
# そのため、時間計算量はO(m + n)です。
# また、追加のメモリは使用せず、与えられた配列内で処理を行うため、空間計算量はO(1)です。


# 単体テスト
def test_solution():
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Test case 1 failed: {nums1}"

    nums1 = [1]
    nums2 = []
    sol.merge(nums1, 1, nums2, 0)
    assert nums1 == [1], f"Test case 2 failed: {nums1}"

    nums1 = [0]
    nums2 = [1]
    sol.merge(nums1, 0, nums2, 1)
    assert nums1 == [1], f"Test case 3 failed: {nums1}"

    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    sol.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6], f"Test case 4 failed: {nums1}"

    nums1 = [2, 0]
    nums2 = [1]
    sol.merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 2], f"Test case 5 failed: {nums1}"

    print("All test cases passed!")


# テスト実行
test_solution()
