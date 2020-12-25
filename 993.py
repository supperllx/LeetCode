# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:  return False
        dq = collections.deque()
        dq.append(root)
        d = {}
        while len(dq):
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    d[node.left.val] = node.val
                if node.right:
                    dq.append(node.right)
                    d[node.right.val] = node.val
            if (x in d) and (y in d) and d[x] != d[y]:  return True
            elif (x in d) or (y in d):  return False
            else:   d.clear()
        return False

