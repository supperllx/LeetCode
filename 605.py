class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:  return True
        length = len(flowerbed)
        res = 0
        if length == 1:
            return True if flowerbed[0] == 0 and n == 1 else False  
        for i in range(length):
            if 1 <= i <= length - 2 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                res += 1
                flowerbed[i] = 1
            elif i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                res += 1
                flowerbed[i] = 1
            elif i == length - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                res += 1
                flowerbed[i] = 1
        return res >= n