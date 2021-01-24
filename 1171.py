# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:    return head
        else:
            cur = head
            cur_sum = 0
            while cur:
                cur_sum += cur.val
                if (cur_sum) == 0:
                    return self.removeZeroSumSublists(cur.next)
                cur = cur.next
            head.next = self.removeZeroSumSublists(head.next)
            return head