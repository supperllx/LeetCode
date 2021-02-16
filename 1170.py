class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            return word.count(min(word))
        
        # fwords = sorted([f(w) for w in words])
        fwords = sorted(map(f, words))
        n = len(words)
        return [n - bisect.bisect(fwords, f(q)) for q in queries]