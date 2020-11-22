# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def addWord(word):
#             nonlocal wordIDs, wordNo
#             if word not in wordIDs:
#                 wordIDs[word] = wordNo
#                 wordNo += 1
        
#         def addEdge(word):
#             nonlocal Edges, wordIDs
#             addWord(word)
#             raw_id = wordIDs[word]
#             chr_l = list(word)
#             for i in range(len(chr_l)):
#                 temp_ch = chr_l[i]
#                 chr_l[i] = '*'
#                 new_word = ''.join(chr_l)
#                 addWord(new_word)
#                 link_id = wordIDs[new_word]
#                 Edges[raw_id].append(link_id)
#                 Edges[link_id].append(raw_id)
#                 chr_l[i] = temp_ch
        
#         wordIDs = {}
#         Edges = collections.defaultdict(list)
#         wordNo = 0
#         for word in wordList:
#             addEdge(word)
#         addEdge(beginWord)
#         if endWord not in wordIDs:    return 0
#         begin_ID, end_ID = wordIDs[beginWord], wordIDs[endWord]
#         dq = collections.deque()
#         dq.append(begin_ID)
#         dist = collections.defaultdict(int)
#         dist[begin_ID] = 0

#         while len(dq):
#             node_id = dq.popleft()
#             if node_id == end_ID: return dist[end_ID] // 2 + 1
#             for neighbor_id in Edges[node_id]:
#                 if neighbor_id not in dist:
#                     dist[neighbor_id] = dist[node_id] + 1
#                     dq.append(neighbor_id)
#         return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word):
            nonlocal wordIDs, wordNo
            if word not in wordIDs:
                wordIDs[word] = wordNo
                wordNo += 1
        
        def addEdge(word):
            nonlocal Edges, wordIDs
            addWord(word)
            raw_id = wordIDs[word]
            chr_l = list(word)
            for i in range(len(chr_l)):
                temp_ch = chr_l[i]
                chr_l[i] = '*'
                new_word = ''.join(chr_l)
                addWord(new_word)
                link_id = wordIDs[new_word]
                Edges[raw_id].append(link_id)
                Edges[link_id].append(raw_id)
                chr_l[i] = temp_ch
        
        wordIDs = {}
        Edges = collections.defaultdict(list)
        wordNo = 0
        for word in wordList:
            addEdge(word)
        addEdge(beginWord)
        if endWord not in wordIDs:    return 0

        begin_ID, end_ID = wordIDs[beginWord], wordIDs[endWord]
        Que_begin, Que_end = collections.deque(), collections.deque()
        Dict_begin, Dict_end = collections.defaultdict(int), collections.defaultdict(int)
        Que_begin.append(begin_ID)
        Que_end.append(end_ID)
        Dict_begin[begin_ID], Dict_end[end_ID] = 0, 0
        while len(Que_begin) and len(Que_end):
            beginSize = len(Que_begin)
            for _ in range(beginSize):
                id1 = Que_begin.popleft()
                if id1 in Dict_end: return (Dict_begin[id1] + Dict_end[id1]) // 2 + 1
                for neighbor_id1 in Edges[id1]:
                    if neighbor_id1 not in Dict_begin:
                        Dict_begin[neighbor_id1] = Dict_begin[id1] + 1
                        Que_begin.append(neighbor_id1)
            
            endSize = len(Que_end)
            for _ in range(endSize):
                id2 = Que_end.popleft()
                if id2 in Dict_begin:   return (Dict_begin[id2] + Dict_end[id2]) // 2 + 1
                for neighbor_id2 in Edges[id2]:
                    if neighbor_id2 not in Dict_end:
                        Dict_end[neighbor_id2] = Dict_end[id2] + 1
                        Que_end.append(neighbor_id2)
        
        return 0

       