# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# 計算量についての説明
# このアルゴリズムの時間計算量はO(n)です。なぜなら、各ノードを一度だけ訪問し、
# 重複をチェックしているためです。ここでnはリンクリストのノードの数です。
# 空間計算量はO(1)です。なぜなら、追加のデータ構造を使用せずに、インプレースで重複を削除しているためです。


# 単体テスト
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_solution():
    sol = Solution()

    # テストケース1
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    result1 = sol.deleteDuplicates(head1)
    assert print_list(result1) == [
        1,
        2,
    ], f"expected [1, 2], but got {print_list(result1)}"

    # テストケース2
    head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    result2 = sol.deleteDuplicates(head2)
    assert print_list(result2) == [
        1,
        2,
        3,
    ], f"expected [1, 2, 3], but got {print_list(result2)}"

    # テストケース3: 空リスト
    head3 = None
    result3 = sol.deleteDuplicates(head3)
    assert print_list(result3) == [], f"expected [], but got {print_list(result3)}"

    # テストケース4: 重複のないリスト
    head4 = ListNode(1, ListNode(2, ListNode(3)))
    result4 = sol.deleteDuplicates(head4)
    assert print_list(result4) == [
        1,
        2,
        3,
    ], f"expected [1, 2, 3], but got {print_list(result4)}"

    # テストケース5: すべて同じ要素
    head5 = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
    result5 = sol.deleteDuplicates(head5)
    assert print_list(result5) == [1], f"expected [1], but got {print_list(result5)}"

    print("全てのテストケースが通過しました。")


test_solution()
