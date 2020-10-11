# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if(head == None or head.next == None):
#             return head
#         else:
#             i_node = ListNode(next = head)
#             p_node = i_node

#             while(p_node.next != None and p_node.next.next != None):
#                 first = p_node.next
#                 second = p_node.next.next
#                 p_node.next = second
#                 first.next = second.next
#                 second.next= first
#                 p_node = first
                
#             return i_node.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):   return head
        else:
            first_node = head
            second_node = head.next
            nxt = self.swapPairs(second_node.next)
            second_node.next = first_node
            first_node.next = nxt
            return second_node