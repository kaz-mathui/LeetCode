import unittest
from typing import List, Optional

# 定義として与えられたTreeNodeクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse the left subtree
            result.append(node.val)  # Visit the root
            inorder(node.right)  # Traverse the right subtree

        inorder(root)
        return result

# 計算量解析:
# 時間計算量 (Time Complexity): O(n)
#   - 各ノードは一度だけ訪問されるため、nはツリーのノード数。
# 空間計算量 (Space Complexity): O(h)
#   - hはツリーの高さ。再帰呼び出しのスタックが最大でツリーの高さに達する。
#   - 最悪の場合（完全に偏ったツリー）では O(n)。バランスの取れたツリーでは O(log n)。

class TestInorderTraversal(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [1, 3, 2])
    
    def test_example2(self):
        root = None
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [])
    
    def test_example3(self):
        root = TreeNode(1)
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [1])
    
    def test_single_left(self):
        root = TreeNode(1, TreeNode(2))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [2, 1])
    
    def test_single_right(self):
        root = TreeNode(1, None, TreeNode(2))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [1, 2])
    
    def test_complete_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [4, 2, 5, 1, 3])

if __name__ == "__main__":
    unittest.main()
