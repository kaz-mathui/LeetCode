# 二分木のノードの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 解法クラスの定義
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


# 計算量の説明
"""
このアルゴリズムは、深さ優先探索 (DFS) を用いて二分木の全てのパスを探索します。
各ノードに対して、左右の子ノードに再帰的に探索を行い、ターゲットの合計に等しいパスが
存在するかを確認します。

時間計算量: O(N)
  - Nは二分木のノードの総数です。各ノードを一度ずつ訪問するため、時間計算量はO(N)です。

空間計算量: O(H)
  - Hは二分木の高さです。再帰の深さは木の高さに比例するため、最悪の場合の空間計算量はO(H)です。
"""


# 単体テスト
def test_hasPathSum():
    # テストケース1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(1)

    assert Solution().hasPathSum(root1, 22) == True, "Test case 1 failed"

    # テストケース2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    assert Solution().hasPathSum(root2, 5) == False, "Test case 2 failed"

    # テストケース3
    root3 = None

    assert Solution().hasPathSum(root3, 0) == False, "Test case 3 failed"

    print("全てのテストケースが成功しました")


# テストの実行
test_hasPathSum()
