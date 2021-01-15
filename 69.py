class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:  return 1
        left, right = 0, x
        while right - left > 1:
            mid = (left + right) // 2
            if (temp := x // mid) == mid:  return mid
            elif temp < mid: right = mid
            else:   left = mid
        return left
        