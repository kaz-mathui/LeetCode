# このアルゴリズムの計算量は O(n) です。ここで、n は文字列 s の長さです。理由は以下の通りです：

# 最初に strip メソッドを使って両端の空白を取り除く操作は O(n) です。
# その後、文字列を空白文字で分割する操作も O(n) です。
# 最後に、リストの最後の要素を取得し、その長さを計算する操作は O(1) です。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 文字列の両端の空白を除去
        s = s.strip()
        # 空白で文字列を分割
        words = s.split(" ")
        # 最後の単語の長さを返す
        return len(words[-1])


import unittest


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_example2(self):
        self.assertEqual(
            self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4
        )

    def test_example3(self):
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello"), 5)

    def test_trailing_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello "), 5)

    def test_leading_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord(" Hello"), 5)

    def test_only_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("      "), 0)


if __name__ == "__main__":
    unittest.main()
