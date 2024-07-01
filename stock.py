from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初期化
        min_price = float("inf")
        max_profit = 0

        # 各日の価格を確認
        for price in prices:
            # 現在の価格が最小価格よりも小さい場合、更新する
            if price < min_price:
                min_price = price
            # 現在の価格で売却する場合の利益を計算し、最大利益を更新する
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# 計算量についての説明
"""
このアルゴリズムの計算量は O(n) です。ここで n は配列 prices の長さです。
アルゴリズムは配列を一度だけスキャンします。それぞれのステップで現在の価格を最小価格と比較し、更新します。
その後、現在の価格で売却する場合の利益を計算し、最大利益を更新します。
よって、全体の計算量は O(n) となり、これは非常に効率的です。
"""


# 単体テスト
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 5)

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_edge_case1(self):
        prices = [1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_edge_case2(self):
        prices = [1, 2]
        self.assertEqual(self.solution.maxProfit(prices), 1)


if __name__ == "__main__":
    unittest.main()
