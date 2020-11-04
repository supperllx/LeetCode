class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        for j, i in prerequisites:
            edges[i].append(j)
            indeg[j] += 1
        res = 0
        dq = collections.deque([i for i in range(numCourses) if indeg[i] == 0])

        while len(dq):
            node = dq.popleft()
            for sub in edges[node]:
                indeg[sub] -= 1
                if indeg[sub] == 0: dq.append(sub)
            res += 1
        return res == numCourses