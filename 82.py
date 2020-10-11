# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:   return head
        else:
            if head.val != head.next.val:   
                head.next = self.deleteDuplicates(head.next)
                return head
            else: #head.val == head.next.val
                while head.next and head.val == head.next.val:  head = head.next
                return self.deleteDuplicates(head.next)
                