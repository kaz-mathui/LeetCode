# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 高さを計算しつつ、平衡性を確認するヘルパー関数
        def check_height(node: TreeNode) -> int:
            # ノードがない場合、木の高さは0
            if not node:
                return 0

            # 左右の子ノードの高さを再帰的に計算
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            # 高さの差が1を超える場合、木は平衡ではない
            if abs(left_height - right_height) > 1:
                return -1

            # 現在のノードの高さを返す
            return max(left_height, right_height) + 1

        # -1が返ってくる場合、木は平衡ではない
        return check_height(root) != -1


# 単体テスト
import unittest


class TestIsBalanced(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertTrue(sol.isBalanced(root))

    def test_example2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        sol = Solution()
        self.assertFalse(sol.isBalanced(root))

    def test_example3(self):
        root = None
        sol = Solution()
        self.assertTrue(sol.isBalanced(root))


if __name__ == "__main__":
    unittest.main()

"""
計算量の説明:

このソリューションの計算量はO(n)です。nは木のノード数を表します。

各ノードで、左右の子ノードの高さを計算し、その結果を使用して現在のノードの高さを計算します。これは各ノードで一度だけ行われるため、全体の計算は木のノード数に比例します。

具体的には、各ノードで行う操作は以下の通りです：
1. 左の子ノードの高さを再帰的に計算します。
2. 右の子ノードの高さを再帰的に計算します。
3. 左右の子ノードの高さの差を確認し、必要に応じて不平衡を検出します。
4. 現在のノードの高さを返します。

この手順は各ノードで一度だけ実行されるため、全体の計算量はO(n)になります。

"""
