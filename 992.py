class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def func(k):
            n = len(A)
            dd = collections.defaultdict(int)
            res = 0
            left, right = 0, 0
            while right < n:
                dd[A[right]] += 1
                while len(dd) > k:
                    dd[A[left]] -= 1
                    if dd[A[left]] == 0:
                        del dd[A[left]]
                    left += 1
                res += (right - left + 1)
                right += 1
            return res
        
        return func(K) - func(K - 1)
