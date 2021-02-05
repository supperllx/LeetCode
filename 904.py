class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        basket = collections.defaultdict(int)
        left, right = 0, 0
        while right < len(tree):
            if len(basket) == 2 and tree[right] not in basket:
                while len(basket) > 1:
                    basket[tree[left]] -= 1
                    if basket[tree[left]] == 0: del basket[tree[left]]
                    left += 1
            basket[tree[right]] += 1
            res = max(res, right - left + 1)
            right += 1
        return res
