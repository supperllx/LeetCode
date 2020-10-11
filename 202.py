class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while n != 1:
            temp = 0
            while n:
                temp += (n%10)**2
                n = n//10
            n = temp
            if n in s:  return False
            else:   s.add(n)
        return True