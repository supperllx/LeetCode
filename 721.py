class unionFind:
    def __init__(self):
        self.d = {}
    
    def find(self, email):
        if email not in self.d: self.d[email] = email
        else:
            if self.d[email] == email:  return email
            else:   self.d[email] = self.find(self.d[email])
        return self.d[email]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:    return 
        elif fx < fy:   self.d[fy] = fx
        else:   self.d[fx] = fy

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = unionFind()
        for acct in accounts:
            for i in range(1, len(acct)):
                uf.union(acct[1], acct[i])
        
        email2index = collections.defaultdict(list)
        for index, u in enumerate(accounts):
            email2index[uf.find(u[1])].append(index)
        
        res = []
        temp = set()
        for indexes in email2index.values():
            for i in indexes:
                name = accounts[i][0]
                temp.update(accounts[i][1:])
            res.append([name] + sorted(list(temp)))
            temp.clear()
        return res
            
