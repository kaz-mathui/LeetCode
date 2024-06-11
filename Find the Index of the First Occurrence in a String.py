import unittest

# haystack の長さを m、needle の長さを n とすると、最悪の場合 O((m - n + 1) * n) になります。
# これは、haystack の各位置で needle と比較するため、m - n + 1 回の比較があり、それぞれの比較で最大 n 回の文字比較が行われるためです。
# 実際の計算量は O(m * n) として考えるのが一般的です。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needleが空の場合は0を返す
        if not needle:
            return 0

        # haystackの長さとneedleの長さを取得
        len_h = len(haystack)
        len_n = len(needle)

        # haystackの中でneedleを探す
        for i in range(len_h - len_n + 1):
            # 部分文字列がneedleと一致するか確認
            if haystack[i : i + len_n] == needle:
                return i

        # 見つからない場合は-1を返す
        return -1


class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)

    def test_example2(self):
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)

    def test_empty_needle(self):
        self.assertEqual(self.solution.strStr("hello", ""), 0)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.solution.strStr("short", "longer"), -1)

    def test_no_occurrence(self):
        self.assertEqual(self.solution.strStr("hello", "world"), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(self.solution.strStr("mississippi", "issip"), 4)

    def test_needle_at_end(self):
        self.assertEqual(self.solution.strStr("findinend", "end"), 6)

    def test_full_string(self):
        self.assertEqual(self.solution.strStr("same", "same"), 0)


if __name__ == "__main__":
    unittest.main()
