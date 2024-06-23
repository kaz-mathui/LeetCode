# 二分木のノードの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ベースケース：もしルートがNoneなら、深さは0です
        if not root:
            return 0

        # 左と右のサブツリーの深さを再帰的に計算します
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # それらのうち最大のものに1を足して（現在のノード分）、返します
        return max(left_depth, right_depth) + 1


# 計算量の説明:
# このアルゴリズムは、各ノードを一度ずつ訪れるので、時間計算量はO(N)です。
# ここで、Nはノードの総数です。また、再帰を使用しているため、空間計算量もO(N)です。
# これは、最悪の場合（木が線形の場合）において、再帰スタックがNの深さになるためです。

# 単体テスト
import unittest


class TestMaxDepth(unittest.TestCase):
    def test_example1(self):
        # テストケース1
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 3)

    def test_example2(self):
        # テストケース2
        root = TreeNode(1)
        root.right = TreeNode(2)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 2)

    def test_empty_tree(self):
        # テストケース3: 空の木
        root = None
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 0)

    def test_single_node(self):
        # テストケース4: 1つのノードのみ
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 1)


if __name__ == "__main__":
    unittest.main()
