# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        dq = collections.deque()
        dq.append(root)
        res = []
        while len(dq):
            size = len(dq)
            temp = []
            for _ in range(size):
                node = dq.popleft()
                if node:
                    dq.append(node.left)
                    dq.append(node.right)
                temp.append(node.val if node else None)
            res+=(temp)
        return res
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == None: return None
        else:
            dq = collections.deque()
            root = TreeNode(data[0])
            dq.append(root)
            p = 1
            while p < len(data):
                node = dq.popleft()
                l_val = data[p]
                r_val = data[p + 1]
                if l_val != None:
                    l_node = TreeNode(l_val)
                    node.left = l_node
                    dq.append(l_node)
                if r_val != None:
                    r_node = TreeNode(r_val)
                    node.right = r_node
                    dq.append(r_node)
                p += 2
            return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))