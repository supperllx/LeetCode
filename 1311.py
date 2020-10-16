class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        ct = collections.Counter()
        dq = collections.deque()
        dq.append(id)
        record = set()
        record.add(id)
        while len(dq): #BFS
            if level == 0:  break
            size = len(dq)
            for i in range(size):
                uid = dq.popleft()
                for fid in friends[uid]:  
                    if fid in record:   continue
                    record.add(fid)  
                    dq.append(fid)
            level -= 1
        for fid in dq:
            for mv in watchedVideos[fid]:   ct[mv] += 1
                
        return [j for i, j in sorted([(y, x) for x, y in ct.most_common()])]
        
        