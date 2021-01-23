# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # print(abs(self.maxDepth(root.right) - self.maxDepth(root.left)))
        if abs(self.maxDepth(root.right) - self.maxDepth(root.left))>1 or not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        else:
            return True
    def maxDepth(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left,right) + 1
        