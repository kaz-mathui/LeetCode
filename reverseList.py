# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            # print('head:',head)
            temp = head.next
            # print('temp:',temp)
            head.next = prev
            prev = head
            print('prev:',prev)
            head = temp
            
        return prev