# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        
#         if head == None or head.next == None:
#             return head
#         elif head.next.next == None:
#             if k%2 == 0:
#                 return head
#             else:
#                 new_head = head.next
#                 head.next = None
#                 new_head.next = head
#                 return new_head
#         else:
#             def rotate(p_head: ListNode):
#                 p_node = p_head
#                 while(p_node.next.next):
#                     p_node = p_node.next

#                 p_node.next.next = p_head
#                 new_head = p_node.next
#                 p_node.next = None
#                 return new_head
            
#             c_head = head
#             length = 0
#             while(c_head):
#                 c_head = c_head.next
#                 length+=1
#             kk = k%length
#             for i in range(kk):
#                 head = rotate(head)
            
#             return head

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if head==None or head.next == None:
#             return head
#         length = 0
#         p_node = head
#         while p_node:
#             length+=1
#             p_node = p_node.next
#         n_rot = k%length
#         if n_rot == 0:
#             return head
#         else:
#             p_node = head
#             for i in range(length - n_rot -1):
#                 p_node = p_node.next
#             new_head = p_node.next
#             p_node.next = None
#             i_node = new_head
#             while i_node.next:
#                 i_node = i_node.next
#             i_node.next = head
#             return new_head

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:   return head
        pre = ListNode(next = head)
        n, p = 0, pre
        while p.next:
            n += 1
            p = p.next
        k %= n
        if k == 0:  return head
        tail, p = p, pre
        for _ in range(n - k):
            p = p.next
        newHead = p.next if p.next else head
        p.next, tail.next = None, head
        return newHead