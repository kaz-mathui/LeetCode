from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# Time Complexity: O(n) - where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(h) - where h is the height of the tree, which is the space used by the system stack during recursion.


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minDepth(self):
        # Example 1
        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(self.solution.minDepth(root1), 2)

        # Example 2
        root2 = TreeNode(2)
        root2.right = TreeNode(3)
        root2.right.right = TreeNode(4)
        root2.right.right.right = TreeNode(5)
        root2.right.right.right.right = TreeNode(6)
        self.assertEqual(self.solution.minDepth(root2), 5)

        # Edge Case: Empty tree
        root3 = None
        self.assertEqual(self.solution.minDepth(root3), 0)

        # Edge Case: Single node tree
        root4 = TreeNode(1)
        self.assertEqual(self.solution.minDepth(root4), 1)


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
