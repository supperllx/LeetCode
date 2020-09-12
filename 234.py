# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        h1 = head #head of first half
        t2 = slow.next
        slow.next = None
        h2 = None #head of second half
        while t2:
            nxt = t2.next
            t2.next = h2
            h2 = t2
            t2 = nxt
        while h2:
            if h2.val != h1.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True
