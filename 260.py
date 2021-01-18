class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        res = [0, 0]
        for n in nums:
            mask ^= n
        mask &= (-mask) # find the rightest '1'
        for n in nums:
            if n & mask == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res
