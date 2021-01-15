class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for ia in range(n):
            if nums[ia] > 0:    break # if a > 0, b & c must also > 0, there will be no answers
            if ia > 0 and nums[ia] == nums[ia - 1]: continue # skip the duplicated a
            ib, ic = ia + 1, n - 1
            while ib < ic:
                cur = nums[ia] + nums[ib] + nums[ic]
                if cur == 0:
                    res.append([nums[ia], nums[ib], nums[ic]])
                    while ib < ic and nums[ib] == nums[ib + 1]: ib += 1 # skip duplicated b
                    ib += 1
                    while ib < ic and nums[ic] == nums[ic - 1]: ic -= 1 # skip duplicated c
                    ic -= 1
                elif cur < 0:
                    last = nums[ib]
                    while ib < ic and nums[ib] == last: ib += 1
                else:
                    last = nums[ic]
                    while ib < ic and nums[ic] == last: ic -= 1
        return res