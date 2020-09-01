# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None:
            return head
        if m == n:
            return head
        pre = ListNode()
        pre.next = head
        p = pre
        i = m
        while i-1:
            p = p.next
            i -= 1
        rev_head = p.next
        temp_tail = None
        for i in range(n - m + 1):
            head_nxt = rev_head.next
            rev_head.next = temp_tail
            temp_tail = rev_head
            rev_head = head_nxt
        p.next = temp_tail
        q = temp_tail
        if q != None:
            while q.next:
                q = q.next
        q.next = rev_head
        return pre.next