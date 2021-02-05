class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right + 1):
            temp_res = True
            for i in str(n):
                if i == '0' or n % int(i) != 0:
                    temp_res = False
                    break
            if temp_res:    res.append(n)
        return res
            

