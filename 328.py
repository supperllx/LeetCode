# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        h1 = ListNode()
        h2 = ListNode()
        l1, l2 = h1, h2
        p = head
        while p.next != None and p.next.next != None:
            l1.next = p
            l2.next = p.next
            l1 = l1.next
            l2 = l2.next
            p = p.next.next
        l1.next = p
        l2.next = p.next
        l1 = l1.next
        l1.next = h2.next
        return h1.next