class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = math.floor(area ** 0.5)
        while W > 0:
            L, remain = divmod(area, W)
            if remain == 0:
                return [L, W]
            W -= 1