# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         curr = head
#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
#         return prev
        
        
        
# #         if head == None or head.next == None:
# #             return head
# #         p = self.reverseList(head.next)
# #         head.next.next = head
# #         head.next = None
# #         return p
    
    
    
    
    
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []

        while head.next:
            stack.append(head)
            head = head.next

        while stack:
            cur = stack.pop()
            cur.next.next = cur
            cur.next = None

        return head
