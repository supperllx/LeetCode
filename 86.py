# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l_1 = ListNode()
        l_2 = ListNode()
        h1 = l_1
        h2 = l_2
        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next
            head = head.next
        h1.next = l_2.next
        h2.next = None
        return l_1.next