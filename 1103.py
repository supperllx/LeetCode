class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # oneTurn = (1 + num_people) * num_people // 2
        # nRoll, remain = divmod(candies, oneTurn)
        # if nRoll:
        #     res = [(i + 1 + i + 1 + ) for i in range(num_people)]
        # for i in range(num_people):

        p = 0
        res = [0] * num_people
        cur = 0
        while candies:
            cur = min(candies, cur + 1)
            res[p] += cur
            candies -= cur
            p = (p + 1) % num_people
        return res