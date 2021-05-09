# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         arr = [False] * len(rooms)
#         dq = collections.deque()
#         dq.append(0)
#         arr[0] = True
#         while dq:
#             curRoom = dq.popleft()
#             for nextRoom in rooms[curRoom]:
#                 if not arr[nextRoom]:
#                     arr[nextRoom] = True
#                     dq.append(nextRoom)
#         return all(arr)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dq = collections.deque()
        dq.append(0)
        total = 0
        visited = 1
        while dq:
            curRoom = dq.popleft()
            total += 1
            for nextRoom in rooms[curRoom]:
                if not (visited & (1 << nextRoom)):
                    dq.append(nextRoom)
                    visited += (1 << nextRoom)
        return total == len(rooms)