# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        ct = collections.Counter()
        max_n = 0
        def get_sum(root):
            if not root:    return 0
            else:
                nonlocal ct, max_n
                l_sum = get_sum(root.left)
                r_sum = get_sum(root.right)
                s = root.val + l_sum + r_sum
                ct[s] += 1
                max_n = max(ct[s], max_n)
                return s
        get_sum(root)
        res = []
        for t in ct.most_common():
            if t[1] == max_n: res.append(t[0])
        return res