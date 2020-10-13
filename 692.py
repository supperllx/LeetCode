# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         cd = collections.Counter(words)
#         hp = [(-cd[i], i) for i in cd.keys()]
#         hp.sort()
#         return [i[1] for i in hp[:k]]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cd = collections.Counter(words)
        hp = sorted([(-cd[i], i) for i in cd.keys()])
        return [i[1] for i in hp[:k]]