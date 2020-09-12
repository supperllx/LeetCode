# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         res = ListNode()
#         head = res
#         min_val = float('inf')
#         min_index = -1
#         while len(lists):
#             min_index = -1
#             min_val = float('inf')
#             for i in range(len(lists)):
#                 if lists[i] == None:
#                     continue
#                 elif lists[i].val <= min_val:
#                     min_val = lists[i].val
#                     min_index = i
            
#             if min_val == float('inf'):
#                 break
#             head.next = lists[min_index]
#             head = head.next
#             if lists[min_index].next == None:
#                 del lists[min_index]
#             else:
#                 lists[min_index] = lists[min_index].next
#         return res.next

class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        res = ListNode()
        head = res
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        while len(h):
            min_node = heapq.heappop(h)
            if min_node[2].next:
                heapq.heappush(h, (min_node[2].next.val, min_node[1], min_node[2].next))
            head.next = min_node[2]
            head = head.next
        return res.next

