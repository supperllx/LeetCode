# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre = ListNode(next = list1)
        pa, pb = pre, list1
        for i in range(b - a):
            pb = pb.next
        for i in range(a):
            pa = pa.next
            pb = pb.next
        pa.next = list2
        while pa.next:
            pa = pa.next
        pa.next = pb.next
        return pre.next
        