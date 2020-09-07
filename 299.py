class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        bull = set()
        a = 0
        b = 0
        for i in range(len(secret)):
            sc = secret[i]
            gc = guess[i]
            if sc == gc:
                a+=1
                bull.add(i)
            else:
                if sc in d:
                    d[sc] += 1
                else:
                    d[sc] = 1
        
        for j in range(len(guess)):
            if j in bull:
                continue
            gc = guess[j]
            if gc in d and d[gc] > 0:
                b+=1
                d[gc] -= 1

        
                    
        return "{a}A{b}B".format(a = a, b =b)