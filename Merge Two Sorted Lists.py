from typing import Optional


# 計算量O(n+m)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # ダミーノードを作成
        dummy = ListNode()
        current = dummy

        # 両リストを走査しながら小さい方の値を持つノードを結果リストに追加
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # どちらかのリストが空になったら、残りのリストを結果リストに追加
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # ダミーノードの次のノードがマージされたリストの開始
        return dummy.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2


def print_linked_list(head):
    """Helper function to print linked list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_merge_two_lists(solution):
    # Helper function to create linked list from list
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Test cases
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([2], [1], [1, 2]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ]

    for i, (list1, list2, expected) in enumerate(test_cases):
        l1 = create_linked_list(list1)
        l2 = create_linked_list(list2)
        merged_head = solution.mergeTwoLists2(l1, l2)
        result = print_linked_list(merged_head)
        # print(result)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed!")


def main():
    solution = Solution()
    test_merge_two_lists(solution)


if __name__ == "__main__":
    main()
