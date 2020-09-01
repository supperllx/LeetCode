# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         pre = ListNode(val = -float('inf'), next = head)
#         p = head
#         pp = pre
#         while p:
#             flag = 0
#             p_nxt = p.next
#             t = pre
#             while t.next != p:
#                 if t.next.val >= p.val:
#                     pp.next = p.next
#                     t_nxt = t.next
#                     t.next = p
#                     p.next = t_nxt
#                     flag = 1
#                     break
#                 t = t.next
#             p = p_nxt
#             if flag == 0:
#                 pp = pp.next
#         return pre.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(val = -float('inf'))
        p = head
        while p:
            p_nxt = p.next
            t = dummy
            while t:
                # if t.next.val >= p.val or t.next == None:
                #     t_nxt = t.next
                #     t.next = p
                #     p.next = t_nxt
                #     break
                # t = t.next
                if t.next != None and t.next.val < p.val:
                    t = t.next
                else:
                    t_nxt = t.next
                    t.next = p
                    p.next = t_nxt
                    break

            p = p_nxt
        return dummy.next
