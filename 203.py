# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(next = head)
        pre = res
        p = head
        while p:
            if p.val != val:
                pre.next = p
                pre = pre.next
            
            p = p.next
        pre.next = None if pre != None else None
        return res.next