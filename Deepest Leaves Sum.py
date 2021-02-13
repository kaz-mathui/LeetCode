# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = {}
        count = 0
        self.dfs(root,ans,count)
        return ans[max(ans)]
    
    def dfs(self,node,ans,count):
        if node:
            if node.left:
                self.dfs(node.left,ans,count+1)
            if node.right:
                self.dfs(node.right,ans,count+1)
        if count not in ans:
            ans[count] = node.val
        else:
            ans[count] += node.val