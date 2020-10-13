class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        res = []
        for w in words:
            temp = w.lower()
            if set(temp).issubset(s1) or set(temp).issubset(s2) or set(temp).issubset(s3):
                res.append(w)
        return res