# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = {}
        stack = []
        p = head
        while p:
            if len(stack) == 0:
                stack.append(p)
            else:
                while len(stack) > 0:
                    if p.val > stack[-1].val:
                        res[stack.pop()] = p.val
                    else:
                        break
                stack.append(p)
            p = p.next
        
        p = head
        ans = []
        while p:
            if p in res:
                ans.append(res[p])
            else:
                ans.append(0)
            p = p.next
        return ans
