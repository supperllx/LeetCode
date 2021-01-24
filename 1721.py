# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for i in range(k - 1):
            p1 = p1.next
        node1 = p1
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        node2 = p2
        node1.val, node2.val = node2.val, node1.val
        return head