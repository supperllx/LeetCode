# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import queue
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         stack = queue.LifoQueue()
#         que = queue.Queue()
#         p_node = head
#         while p_node:
#             que.put(p_node)
#             p_node = p_node.next
#             if p_node == None:
#                 break
#             stack.put(p_node)
#             p_node = p_node.next
#         res = ListNode()
#         while (not stack.empty()) and (not que.empty()):
#             res.next = que.get()
#             res = res.next
#             res.next = stack.get()
#             res = res.next
#             res.next = None

#         return res.next

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         if head == None or head.next == None:
#             return head
#         p = head
#         while p.next.next:
#             p = p.next
#         last = p.next
#         p.next = None
#         last.next = head.next
#         head.next = last
#         self.reorderList(last.next)

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next
        r2 = None
        slow.next = None
        p2 = h2
        while p2:
            r2, p2.next, p2  = p2, r2, p2.next
            # p_node.next, p_node, new_head = new_head, p_node.next, p_node

        p1 = head
        p2 = r2
        new_head = ListNode()
        while p1 != None:
            p1_nxt = p1.next
            p2_nxt = p2.next if p2 else None
            new_head.next = p1
            new_head = new_head.next
            new_head.next = p2
            new_head = new_head.next
            p1 = p1_nxt
            p2 = p2_nxt
            

        return head

