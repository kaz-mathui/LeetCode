# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # 両方のサブツリーが空の場合、対称です
            if not t1 and not t2:
                return True
            # どちらか一方のサブツリーのみが空の場合、対称ではありません
            if not t1 or not t2:
                return False
            # ルートノードの値が同じで、サブツリーが鏡像であるかどうかをチェック
            return (
                (t1.val == t2.val)
                and isMirror(t1.right, t2.left)
                and isMirror(t1.left, t2.right)
            )

        return isMirror(root, root)


# 計算量についての説明:
# 時間計算量: O(n)
# 各ノードを一度だけ訪問するため、時間計算量はノード数に比例します。

# 空間計算量: O(n)
# 最悪の場合（完全に平衡した木）には再帰呼び出しのスタックが最大でツリーの高さになります。
# ツリーの高さは最悪の場合で O(n) となります。

# 単体テスト
import unittest


class TestSolution(unittest.TestCase):
    def test_isSymmetric(self):
        sol = Solution()

        # テストケース1: 対称的なツリー
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(3)
        root1.left.right = TreeNode(4)
        root1.right.left = TreeNode(4)
        root1.right.right = TreeNode(3)
        self.assertTrue(sol.isSymmetric(root1))

        # テストケース2: 非対称的なツリー
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)
        root2.left.right = TreeNode(3)
        root2.right.right = TreeNode(3)
        self.assertFalse(sol.isSymmetric(root2))


if __name__ == "__main__":
    unittest.main()
