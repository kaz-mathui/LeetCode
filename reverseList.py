# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # while head:
        #     # print('head:',head)
        #     temp = head.next
        #     # print('temp:',temp)
        #     head.next = prev
        #     prev = head
        #     print('prev:',prev)
        #     head = temp
            
        # return prev
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    #  if (head == null || head.next == null) return head;
    # ListNode p = reverseList(head.next);
    # head.next.next = head;
    # head.next = null;
    # return p;