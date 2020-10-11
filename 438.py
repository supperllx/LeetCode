class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        def sTOl(s):    
            d = [0] * 26
            for ch in s:
                d[ord(ch) - 97] += 1
            return d
        pl = sTOl(p)
        sl = sTOl(s[0:len(p)])
        res = []

        left, right = 0, len(p) - 1
        while right < len(s) - 1:
            if sl == pl:    res.append(left)
            sl[ord(s[left]) - 97] -= 1
            left += 1
            right += 1
            sl[ord(s[right]) - 97] += 1
        
        if sl == pl:    res.append(left)
            
        return res