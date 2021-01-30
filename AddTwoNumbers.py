# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        l1_num = 0
        l2_num = 0
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        for i in range(len(l1_list)):
            l1_num += l1_list[i] * (10 ** i)
        for i in range(len(l2_list)):
            l2_num += l2_list[i] * (10 ** i)
        total = l1_num + l2_num
        digits = len(str(total))
        node = ListNode()
        head = ListNode(total % 10,node)
        print(total)
        for i in range(digits):
            total = int(total / 10)
            node.val = total % 10
            if total < 10:
                break
            node.next = ListNode()
            node = node.next
        return head
            
        
        