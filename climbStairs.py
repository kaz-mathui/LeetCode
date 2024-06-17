class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # 初期値の設定
        prev1, prev2 = 1, 2
        
        # nが3以上の場合の計算
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2

# 単体テスト
import unittest

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_climb_stairs(self):
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)
        self.assertEqual(self.solution.climbStairs(4), 5)
        self.assertEqual(self.solution.climbStairs(5), 8)
        self.assertEqual(self.solution.climbStairs(10), 89)
        self.assertEqual(self.solution.climbStairs(1), 1)
        self.assertEqual(self.solution.climbStairs(45), 1836311903)

if __name__ == '__main__':
    unittest.main()
