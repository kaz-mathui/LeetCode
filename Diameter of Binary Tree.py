# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            self.ans = max(self.ans,left+right)
            return max(left,right) + 1
        
        dfs(root)
        return self.ans