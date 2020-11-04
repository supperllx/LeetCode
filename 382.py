# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.capacity = 1
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        # res = None
        res = []
        p = self.head
        while p:
            # count += 1
            # r = random.randint(1, count)
            # if r == count:  res = p
            # p = p.next
            count += 1
            if count <= self.capacity:  res.append(p.val)
            else:
                r = random.randint(1, count)
                if r <= self.capacity:  res[r - 1] = p.val
            p = p.next
        return res[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()