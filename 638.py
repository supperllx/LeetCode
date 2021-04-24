class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @functools.cache
        def func(needList):
            total = 0
            for i, need in enumerate(needList):
                total += need * price[i]
            
            for pack in special:
                newNeed = []
                for i in range(len(needList)):
                    if (temp := (needList[i] - pack[i])) < 0:   break
                    else:   newNeed.append(temp)
                
                if len(newNeed) == len(needList):
                    total = min(total, pack[-1] + func(tuple(newNeed)))
            return total
        return func(tuple(needs))