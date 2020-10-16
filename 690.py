"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for e in employees: d[e.id] = e
        def func(uid):
            user = d[uid]
            if len(user.subordinates) == 0: return user.importance
            else:
                return user.importance + sum([func(i) for i in user.subordinates])
        return func(id)
        