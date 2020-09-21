# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            slow, fast = head, head.next
            while fast != None and fast.next != None:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None
            left, right = self.sortList(head), self.sortList(mid)
            res = ListNode(0)
            p = res
            while (left != None) and (right != None):
                if left.val < right.val:
                    p.next = left
                    left = left.next
                else:
                    p.next = right
                    right = right.next
                p = p.next
            p.next = left if left != None else right
            return res.next