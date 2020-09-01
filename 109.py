# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         def get_root(head):
#             if head == None:
#                 return head
#             elif head.next == None:
#                 return head
#             fast = head
#             slow = head
#             pre_slow = ListNode(next = head)
#             while fast != None and fast.next != None:
#                 slow = slow.next
#                 pre_slow = pre_slow.next
#                 fast = fast.next.next
#             pre_slow.next = None
#             return slow
#         def func(head):
#             if head == None:
#                 return None
#             elif head.next == None:
#                 return TreeNode(val = head.val)
#             else:
#                 root = get_root(head)
#                 left_head = head
#                 right_head = root.next if root else None
#                 t_root = TreeNode(val = root.val)
#                 t_root.left = func(left_head)
#                 t_root.right = func(right_head)
#                 return t_root
#         return func(head)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        elif head.next == None:
            return TreeNode(val = head.val)
        else:
            slow = head
            pre_slow = ListNode(next = head)
            fast = head
            while fast != None and fast.next != None:
                slow = slow.next
                pre_slow = pre_slow.next
                fast = fast.next.next
            pre_slow.next = None
            left_head = head
            right_head = slow.next
            root = TreeNode(val = slow.val)
            root.left = self.sortedListToBST(left_head)
            root.right = self.sortedListToBST(right_head)
            return root
            

