# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        while head:
            head_nxt = head.next
            head.next = res
            res = head
            head = head_nxt

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
#         else:
#             new_head = self.reverseList(head.next)
#             head.next.next = head
#             head.next = None
#         return new_head