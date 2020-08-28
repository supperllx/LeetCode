# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p_node = head
        new_head = None
        while p_node:
            p_node.next, p_node, new_head = new_head, p_node.next, p_node
        return new_head

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
#         else:
#             new_head = self.reverseList(head.next)
#             head.next.next = head
#             head.next = None
#         return new_head