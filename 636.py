# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
#         stack = []
#         arr = [0 for _ in range(n)]
#         for log in logs:
#             th_id, status, curTime = log.split(':')
#             th_id, curTime = int(th_id), int(curTime)
#             if status == 'end':
#                 arr[th_id] += (curTime - stack[-1][2] + 1)
#                 stack.pop()
#                 if stack:   stack[-1][2] = curTime + 1
#             else:
#                 if not stack:
#                     stack.append([th_id, status, curTime])
#                 else:
#                     arr[stack[-1][0]] += (curTime - stack[-1][2])
#                     stack.append([th_id, status, curTime])
#         return arr

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        arr = [0 for _ in range(n)]
        for log in logs:
            th_id, status, curTime = log.split(':')
            th_id, curTime = int(th_id), int(curTime)
            if status == 'end':
                arr[th_id] += (curTime - stack[-1][2] + 1)
                stack.pop()
                if stack:   stack[-1][2] = curTime + 1 # update the stack[-1]
            else: # status == 'start'
                if stack: # stack[-1].status must be 'start'
                    arr[stack[-1][0]] += (curTime - stack[-1][2])
                stack.append([th_id, status, curTime])
        return arr