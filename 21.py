# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p_node = l1
        q_node = l2
        if l1==None and l2 == None:
            return l1
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = p_node
            p_node = p_node.next
        else:
            head = q_node
            q_node = q_node.next
        ans = head
        while p_node != None or q_node != None:
            if p_node == None and q_node != None:
                head.next = q_node
                break
            elif q_node == None and p_node != None:
                head.next = p_node
                p_node = p_node.next
                break
            
            if(p_node.val <= q_node.val):
                head.next = p_node
                p_node = p_node.next
                head = head.next
            else:
                head.next = q_node
                q_node = q_node.next
                head = head.next
                
        return ans
            
            