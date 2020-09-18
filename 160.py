# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         i_a = 0
#         i_b = 0
#         p_a = headA
#         p_b = headB
#         while p_a != None or p_b != None:
#             if p_a == p_b:
#                 return p_a
#             if p_a:
#                 p_a = p_a.next
#                 i_a += 1
#             if p_b:
#                 p_b = p_b.next
#                 i_b += 1
        
#         diff = abs(i_a - i_b)

#         (l_h, s_h) = (headA, headB) if i_a >= i_b else (headB, headA)
#         for i in range(diff):
#             l_h = l_h.next

#         while l_h:
#             if l_h == s_h:
#                 break
#             l_h = l_h.next
#             s_h = s_h.next
#         return l_h

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         path = set()
#         while headA:
#             path.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in path:
#                 return headB
#             headB = headB.next
#         return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 != None else headB
            p2 = p2.next if p2 != None else headA
        return p1