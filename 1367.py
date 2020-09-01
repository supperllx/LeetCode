# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def func(self, head: ListNode, root: TreeNode):
        if head == None:
            return True
        elif root == None:
            return False
        else:
            if head.val == root.val:
                return self.func(head.next, root.left) or self.func(head.next, root.right)
            else:
                return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root == None:
            return False
        else:
            return self.func(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        