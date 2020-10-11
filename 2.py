# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode()
        head = pre
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            head.next = ListNode((v1 + v2 + carry)%10)
            carry = (v1 + v2 + carry) // 10
            head = head.next
            if l1:  l1 = l1.next
            if l2:  l2 = l2.next
        return pre.next
            
