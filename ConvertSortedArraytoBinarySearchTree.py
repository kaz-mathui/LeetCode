from typing import List, Optional


# 二分木のノードの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 内部関数を使って再帰的にBSTを構築する
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # 中央要素を選択
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # 左右のサブツリーを再帰的に構築
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)


# 計算量についての説明:
# このアルゴリズムは、ソートされた配列を使って高さバランスの取れたBSTを構築します。
# 1. 配列の中央要素を選択する操作はO(1)です。
# 2. 左右のサブツリーを再帰的に構築するため、各再帰呼び出しは配列のサイズを半分に減らします。
# 3. 再帰的な分割の深さは配列の長さnに対してO(log n)です。
# 4. 各レベルで全体の要素を一度訪れるため、各レベルの操作はO(n)です。
# したがって、全体の時間計算量はO(n)です。


# 単体テスト
def preOrder(node: Optional[TreeNode]) -> List[int]:
    if node is None:
        return []
    return [node.val] + preOrder(node.left) + preOrder(node.right)


# テストケース1
nums1 = [-10, -3, 0, 5, 9]
solution = Solution()
bst1 = solution.sortedArrayToBST(nums1)
print(preOrder(bst1))  # 出力例: [0, -3, -10, 9, 5]

# テストケース2
nums2 = [1, 3]
bst2 = solution.sortedArrayToBST(nums2)
print(preOrder(bst2))  # 出力例: [1, 3] または [3, 1]
