class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        elif len(nums) == 1:
            return nums
        else:
            # i = random.randint(0, len(nums) - 1)
            i = 0
            left, right = list(), list()
            for n in nums[1:]:
                if n <= nums[i]:    left.append(n)
                else:   right.append(n)
            return self.sortArray(left) + [nums[i]] + self.sortArray(right)