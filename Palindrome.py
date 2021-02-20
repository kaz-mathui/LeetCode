# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     # def isPalindrome(self, head: ListNode) -> bool:
#     #     # vals = []
#     #     # current_node = head
#     #     # while current_node is not None:
#     #     #     vals.append(current_node.val)
#     #     #     current_node = current_node.next
#     #     # return vals == vals[::-1]
#     #     self.front_pointer = head

#     #     def recursively_check(current_node=head):
#     #         if current_node is not None:
#     #             if not recursively_check(current_node.next):
#     #                 return False
#     #             if self.front_pointer.val != current_node.val:
#     #                 return False
#     #             self.front_pointer = self.front_pointer.next
#     #         return True

#     #     return recursively_check()
    
#     def isPalindrome(self, head: ListNode) -> bool:
#         if head is None:
#             return True

#         # Find the end of first half and reverse second half.
#         first_half_end = self.end_of_first_half(head)
#         second_half_start = self.reverse_list(first_half_end.next)

#         # Check whether or not there's a palindrome.
#         result = True
#         first_position = head
#         second_position = second_half_start
#         while result and second_position is not None:
#             if first_position.val != second_position.val:
#                 result = False
#             first_position = first_position.next
#             second_position = second_position.next

#         # Restore the list and return the result.
#         # first_half_end.next = self.reverse_list(second_half_start)
#         return result    

#     def end_of_first_half(self, head):
#         fast = head
#         slow = head
#         while fast.next is not None and fast.next.next is not None:
#             fast = fast.next.next
#             slow = slow.next
#         return slow

#     def reverse_list(self, head):
#         previous = None
#         current = head
#         while current is not None:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node
        # return previous


# PlayNice

def isPalindrome(self, head):
    rev = None
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    tail = head.next if fast else head
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
    return isPali