class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for ia in range(n):
            if ia > 0 and nums[ia - 1] == nums[ia]: continue 
            for ib in range(ia + 1, n):
                if ib > ia + 1 and nums[ib - 1] == nums[ib]: continue
                left, right = ib + 1, n - 1
                while left < right:
                    cur = nums[ia] + nums[ib] + nums[left] + nums[right]
                    if cur == target:
                        res.append([nums[ia], nums[ib], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:    left += 1
                        left += 1
                        while right > left and nums[right] == nums[right - 1]:  right -= 1
                        right -= 1
                    elif cur < target:
                        last = nums[left]
                        while left < right and nums[left] == last:  left += 1
                    else:
                        last = nums[right]
                        while right > left and nums[right] == last: right -= 1
        
        return res


