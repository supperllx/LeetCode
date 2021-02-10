class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]: # Linked List
        p = collections.deque([i for i in range(1, m + 1)])
        res = []
        for i, q in enumerate(queries):
            j = p.index(q)
            del p[j]
            p.appendleft(q)
            res.append(j)
        return res

# class Solution:
#     def processQueries(self, queries: List[int], m: int) -> List[int]: # Array
#         p = [i for i in range(1, m + 1)]
#         res = []
#         for i, q in enumerate(queries):
#             j = p.index(q)
#             del p[j]
#             p = [q] + p
#             res.append(j)
#         return res