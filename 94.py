class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def func(p_root):
            nonlocal ans
            if p_root:
                if p_root.left:
                    func(p_root.left)
                ans.append(p_root.val)
                if p_root.right:
                    func(p_root.right)
        func(root)
        return ans