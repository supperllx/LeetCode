# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        d = {}
        p = head
        while p:
            while stack and stack[-1].val < p.val:
                d[stack.pop()] = p.val
            stack.append(p)
            p = p.next
        p = head
        while p:
            res.append(d[p] if p in d else 0)
            p = p.next
        return res

