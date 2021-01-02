# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         left, right = float('inf'), -float('inf')
#         for bd in buildings:
#             left = min(left, bd[0])
#             right = max(right, bd[1])
#         hp = []
#         res = []
#         d_l = collections.defaultdict(list)
#         for bd in buildings:
#             d_l[bd[0]].append(bd)
#         for i in range(left, right + 1):
#             if i in d_l:
#                 for bd in d_l[i]:
#                     heapq.heappush(hp, (-bd[2], -bd[1]))
#             while len(hp) and (-hp[0][1]) <= i:
#                 heapq.heappop(hp)
#             active = hp[0] if hp else [0, -1]
#             if (not res) or (res[-1][1] != -active[0]):
#                 res.append([i, -active[0]])
        
#         return res

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # get all the non-duplicated key points to be checked
        s = set()
        for bd in buildings:
            s.add(bd[0])
            s.add(bd[1])
        s = list(s)
        heapq.heapify(s)
            
        hp = [] # large heap [height, right_position]
        res = []
        d_l = collections.defaultdict(list) # dict: left_position -> building
        for bd in buildings:
            d_l[bd[0]].append(bd)
            
        while len(s):
            # get current key point
            i = heapq.heappop(s)
            # add all new available buildings if exist into the heap
            if i in d_l:
                for new_bd in d_l[i]:
                    heapq.heappush(hp, (-new_bd[2], -new_bd[1]))
            # delete all out-ranged buildings
            while len(hp) and (-hp[0][1]) <= i:
                heapq.heappop(hp)
            # get current highest building
            active = hp[0] if hp else [0, -1]
            # if it's start point or the highest building has changed, add new height into result
            if (not res) or (res[-1][1] != -active[0]):
                res.append([i, -active[0]])
        
        return res
