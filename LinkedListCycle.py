# ハッシュを使う
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         nodes_seen = set()
#         while head is not None:
#             if head in nodes_seen:
#                 return True
#             nodes_seen.add(head)
#             head = head.next
#         return False

# 速いランナーと遅いランナーで比較する
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True