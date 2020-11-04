class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:  return []
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for j, i in prerequisites:
            edges[i].append(j)
            indeg[j] += 1
        
        dq = collections.deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []
        while len(dq):
            node = dq.popleft()
            res.append(node)
            for sub in edges[node]:
                indeg[sub] -= 1
                if indeg[sub] == 0: dq.append(sub)
        
        return res if len(res) == numCourses else []