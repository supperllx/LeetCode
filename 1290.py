# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        ans = 0
        while p:
            ans = (ans<<1) + p.val
            p = p.next
        return ans