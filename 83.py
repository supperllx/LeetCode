# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
#         elif head.next.next == None:
#             if head.val == head.next.val:
#                 head.next = None
#             return head
        
#         p_node = head
#         while(p_node.next != None):
#             if p_node.val == p_node.next.val:
#                 if p_node.next.next != None:
#                     p_node.next = p_node.next.next
#                 else:
#                     p_node.next = None
#             else:
#                 p_node = p_node.next
#         return head
            

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p != None and p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
                continue
            p = p.next
        return head
        