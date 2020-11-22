"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:    return None
#         d = {}
#         dq = collections.deque()
#         dq.append(node)
#         while len(dq):
#             raw_node = dq.popleft()
#             if raw_node not in d:
#                 d[raw_node] = Node(raw_node.val)
#             for neighbor in raw_node.neighbors:
#                 if neighbor not in d:
#                     dq.append(neighbor)
        
#         dq.append(node)
#         visited = set()
#         visited.add(node)
#         while len(dq):
#             raw_node = dq.popleft()
#             visited.add(raw_node)
#             new_node = d[raw_node]
#             new_node.neighbors = []
#             for raw_neighbor in raw_node.neighbors:
#                 new_node.neighbors.append(d[raw_neighbor])
#                 if raw_neighbor not in visited:
#                     dq.append(raw_neighbor)
#         return d[node]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':  #BFS
        if not node:    return None
        d = {}
        dq = collections.deque()
        dq.append(node)
        while len(dq):
            raw_node = dq.popleft()
            if raw_node not in d:
                d[raw_node] = Node(raw_node.val, [])
            for raw_neighbor in raw_node.neighbors:
                if raw_neighbor not in d:
                    d[raw_neighbor] = Node(raw_neighbor.val, [])
                    dq.append(raw_neighbor)
                d[raw_node].neighbors.append(d[raw_neighbor])
        return d[node]
