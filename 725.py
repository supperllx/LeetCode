# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        p = root
        while p:
            n += 1
            p = p.next
        interval, remain = divmod(n, k)
        res = []
        p = root
        print(interval, remain)
        for _ in range(k):
            head = p
            if remain > 0:
                cur_interval = interval + 1
                remain -= 1
            else:   cur_interval = interval
            for _ in range(cur_interval - 1):
                p = p.next
            if p:   p.next, p = None, p.next
            res.append(head)
        
        return res
            