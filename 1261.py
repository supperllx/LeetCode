# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.s = set()
        root.val = 0
        def func(root):
            if root:
                self.s.add(root.val)
                if root.left:   root.left.val = 2 * root.val + 1
                if root.right:  root.right.val = 2 * root.val + 2
                func(root.left)
                func(root.right)
                # return root
        # self.root = func(root)
        func(root)
        

    def find(self, target: int) -> bool:
        return target in self.s
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)