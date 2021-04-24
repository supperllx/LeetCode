class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def func(x, y):
            s1, s2 = x + y, y + x
            if s1 == s2:    return 0
            elif s1 > s2:   return 1
            else:   return -1

        nums = list(map(str, nums))
        nums.sort(key = functools.cmp_to_key(func), reverse = True)
        res = ''.join(nums).lstrip('0')
        if not res: res += '0'
        return res