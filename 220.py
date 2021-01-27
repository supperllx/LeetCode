class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        d = collections.defaultdict(set)

        for i, num in enumerate(nums):
            d[num].add(i)
        for index, num in enumerate(nums):
            if k + 1 < t:
                for i in range(1, k + 1):
                    if (index + i) < n and abs(nums[index] - nums[index + i]) <= t:
                        # print(index, i)
                        return True
                    if (index - i) >= 0 and abs(nums[index] - nums[index - i]) <= t:
                        # print(index, i)
                        return True
            else:
                # if t == 0:
                #     print(len(d[num]))
                #     if len(d[num]) > 1: return True
                for i in range(t + 1):
                    if len(d[num - i]) > k:
                        for j in range(1, k + 1):
                            if index + j in d[num - i]: return True
                            if index - j in d[num - i]: return True
                    else:
                        for index2 in d[num - i]:
                            if 1 <= abs(index - index2) <= k:   return True
                        for index2 in d[num + i]:
                            if 1 <= abs(index - index2) <= k:   return True
        return False