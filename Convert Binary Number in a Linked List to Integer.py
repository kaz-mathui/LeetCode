# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        lists = []
        while head:
            lists += head.val,
            head = head.next
        ans = 0
        print(lists)
        for i in range(len(lists)):
            print(lists[i])
            
            ans += lists[i] * 2**(len(lists)-i-1)
            print(ans)
        return ans
