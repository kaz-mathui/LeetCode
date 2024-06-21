# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # もし両方のノードが空であれば、木は同じであるとみなされます。
        if not p and not q:
            return True
        # どちらか一方だけが空であれば、木は異なるとみなされます。
        if not p or not q:
            return False
        # 現在のノードの値が異なれば、木は異なるとみなされます。
        if p.val != q.val:
            return False
        # 再帰的に左の子ノードと右の子ノードを比較します。
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 計算量の詳細説明:
# このアルゴリズムは二分木の各ノードを一度だけ訪問します。したがって、時間計算量はO(N)です。
# ここで、Nは二分木のノード数です。
# 空間計算量もO(N)です。再帰呼び出しのスタックサイズが木の高さに比例するためです。
# 平衡木の場合、高さはO(log N)ですが、最悪の場合（片側に偏った木など）ではO(N)になります。

# 単体テスト
import unittest


class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trees_are_same(self):
        # 木 p: [1, 2, 3]
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        # 木 q: [1, 2, 3]
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        self.assertTrue(self.solution.isSameTree(p, q))

    def test_trees_are_different_structure(self):
        # 木 p: [1, 2]
        p = TreeNode(1)
        p.left = TreeNode(2)

        # 木 q: [1, null, 2]
        q = TreeNode(1)
        q.right = TreeNode(2)

        self.assertFalse(self.solution.isSameTree(p, q))

    def test_trees_are_different_values(self):
        # 木 p: [1, 2, 1]
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)

        # 木 q: [1, 1, 2]
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)

        self.assertFalse(self.solution.isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()
