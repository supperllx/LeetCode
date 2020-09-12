# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        else:
            i_node = ListNode(next = head)
            p_node = i_node

            while(p_node.next != None and p_node.next.next != None):
                first = p_node.next
                second = p_node.next.next
                p_node.next = second
                first.next = second.next
                second.next= first
                p_node = first
                
            return i_node.next
        