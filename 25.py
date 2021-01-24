# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        if not head or not head.next:   return head
        else:
            nxt = head.next
            new_head = self.reverse(head.next)
            nxt.next, head.next = head, None
            return new_head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:   return head
        p = head
        for i in range(k - 1):
            p = p.next
            if not p:   return head
        nxt = p.next
        p.next = None
        new_head = self.reverse(head)
        head.next = self.reverseKGroup(nxt, k)
        return new_head


        
