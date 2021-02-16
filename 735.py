# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         if not asteroids:   return asteroids
#         arr = []
#         i = 0
#         while i < len(asteroids):
#             if i < len(asteroids) - 1 and asteroids[i] > 0 and asteroids[i + 1] < 0:
#                 if (w1 := abs(asteroids[i])) > (w2 := abs(asteroids[i + 1])):
#                     arr.append(asteroids[i])
#                 elif w1 < w2:
#                     arr.append(asteroids[i + 1])
#                 i += 1
#             else:
#                 arr.append(asteroids[i])
#             i += 1
#         if len(asteroids) == len(arr):
#             return arr
#         else:
#             return self.asteroidCollision(arr)

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         while True:
#             stack = []
#             for a in asteroids:
#                 if not stack:
#                     stack.append(a)
#                 elif stack[-1] > 0 and a < 0:
#                     if (w1 := abs(stack[-1])) < (w2 := abs(a)):
#                         stack.pop()
#                         stack.append(a)
#                     elif w1 == w2:
#                         stack.pop()
#                 else:
#                     stack.append(a)
#             if not stack or len(stack) == len(asteroids):
#                 return stack
#             else:
#                 asteroids = stack
        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack