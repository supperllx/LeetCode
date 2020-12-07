class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0, 10:0}
        for b in bills:
            if b == 5:  d[5] += 1
            elif b == 10:
                if d[5] == 0:   return False
                else:
                    d[5] -= 1
                    d[10] += 1
            else:
                if d[5] > 0 and d[10] > 0:
                    d[5] -= 1
                    d[10] -= 1
                elif d[10] == 0:
                    if d[5] >= 3:   d[5] -= 3
                    else:   return False
                else:
                    return False
        return True