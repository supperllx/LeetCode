class UnionFind:
    def __init__(self):
        self.d = dict()
    def find(self, word):
        if word not in self.d:  self.d[word] = word
        elif self.d[word] != word:
            self.d[word] = self.find(self.d[word])
        return self.d[word]
    def union(self, w1, w2):
        f1, f2 = self.find(w1), self.find(w2)
        if f1 < f2: self.d[f2] = f1
        elif f1 > f2:   self.d[f1] = f2

class Solution:
    # def enumerate_allSimilar(self, s, uf):
    #     arr = list(s)
    #     for i in range(len(arr)):
    #         for j in range(i + 1, len(arr)):
    #             arr[i], arr[j] = arr[j], arr[i]
    #             uf.union(s, ''.join(arr))
    #             arr[i], arr[j] = arr[j], arr[i]


    def isSimilar(self, s1, s2):
        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:  count += 1
            if count > 2:   return False
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()

        # if len(strs) >= len(strs[0]): # number of str > str length, enumerate all the similar strings for each str
        #     for s in strs:
        #         self.enumerate_allSimilar(s, uf)
            
        #     record = set()
        #     for s in strs:
        #         record.add(uf.find(s))
        #     return len(record)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if self.isSimilar(s1 := strs[i], s2 := strs[j]):
                    uf.union(s1, s2)

        record = set()
        for s in strs:
            record.add(uf.find(s))
        return len(record)
