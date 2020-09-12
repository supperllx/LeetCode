# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        m_node = head
        n_node = head
        while m_node != None and n_node != None:
            m_node = m_node.next
            n_node = n_node.next
            if m_node == None or n_node == None:
                return False
            n_node = n_node.next

            if(m_node == n_node):
                return True 
        
        return False
