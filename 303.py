class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self.preSum[i + 1] = self.preSum[i] + n



    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j + 1] - self.preSum[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)