# class ListNode:
#     def __init__(self, url, prev = None, next = None):
#         self.url = url
#         self.prev = prev
#         self.next = next
    
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.cursor = ListNode(homepage)


#     def visit(self, url: str) -> None:
#         node = ListNode(url)
#         p = self.cursor.next
#         self.cursor.next, node.prev = node, self.cursor
#         self.cursor = node
#         while p:
#             Del_Node = p
#             p = p.next
#             del Del_Node

#     def back(self, steps: int) -> str:
#         for _ in range(steps):
#             if not self.cursor.prev:
#                 break
#             self.cursor = self.cursor.prev
#         return self.cursor.url


#     def forward(self, steps: int) -> str:
#         for _ in range(steps):
#             if not self.cursor.next:
#                 break
#             self.cursor = self.cursor.next
#         return self.cursor.url


class BrowserHistory:

    def __init__(self, homepage: str):
        self.History = [homepage]
        self.cursor = 0

    def visit(self, url: str) -> None:
        while self.History[-1] != self.History[self.cursor]:
            self.History.pop()
        self.History.append(url)
        self.cursor += 1


    def back(self, steps: int) -> str:
        self.cursor = self.cursor - steps if self.cursor >= steps else 0
        return self.History[self.cursor]


    def forward(self, steps: int) -> str:
        self.cursor = self.cursor + steps if self.cursor + steps < len(self.History) else len(self.History) - 1
        return self.History[self.cursor]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)