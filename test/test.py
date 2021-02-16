import collections
import heapq
import sortedcontainers
import sortedcollections
import bisect

class obj:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('on deletion')

def down_print(n):
    if n <= 0: return 0
    else:
        print(n)
        return down_print(n - 1)

def q_sort(arr):
    if not arr: return arr
    else:
        cur = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i <= cur: left.append(i)
            else: right.append(i)
        return q_sort(left) + [cur] + q_sort(right)

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n-1) + func(n-2)

def fab(n: int) -> int: 
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return fab(n-1) + fab(n-2)

def coin(n: int):
    l = [float('inf')] * (n+1)
    l[0] = 0

    for i in range(1,n+1):
        p1 = l[i -2] if i-2 >= 0 else float('inf')
        p2 = l[i -5] if i-5 >=0 else float('inf')
        p3 = l[i - 7] if i - 7 >= 0 else float('inf')
        l[i] = min(p1, p2, p3) + 1
    return l[n]

def coin_2(n:int):
    d = {}
    def func(n: int):
        res = float('inf')
        nonlocal d
        if n in d:
            return d[n]
        if n == 0:
            res = 0
        if n >= 2:
            res = min(func(n - 2) + 1, res)
        if n >= 5:
            res = min(func(n-5)+1, res)
        if n >= 7:
            res = min(func(n-7)+ 1, res)
        d[n] = res
        return res
    return func(n)

def frog(l: list) -> bool:
    dp = [False] * len(l)
    dp[0] = True
    for i in range(1, len(l)):
        for j in range(0, i):
            dp[i] = dp[i] or (dp[j] and j + l[j] >= i)
            if dp[i] == True:   break
    return dp[-1]

def max_product_subarray(nums: list) -> list:
    n = len(nums)
    dp_max = [0 for _ in range(n)]
    dp_min = [0 for _ in range(n)]
    dp_max[0], dp_min[0] = nums[0], nums[0]
    for i in range(1, n):
        dp_max[i] = max(dp_min[i - 1] * nums[i], max(dp_max[i - 1] * nums[i], nums[i]))
        dp_min[i] = min(dp_max[i - 1] * nums[i], min(dp_min[i - 1] * nums[i], nums[i]))
    return max(dp_max)

def recursive_reduction(array, size):
    if size == 1: return array[0]
    else:
        stride = size // 2
        for i in range(stride):
            array[i] += array[i + stride]
        return recursive_reduction(array, stride)

def test_arg(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

def total_prefix(s: str) -> int:
    res = len(s)
    def func(p, string):
        print(string, s[p])
        nonlocal res
        if p >= len(s):
            return
        new_string = ''.join(string.split(s[p]))
        if len(string) == len(new_string):
            # print(string, new_string)
            return
        else:
            print(string, new_string, (len(string) - len(new_string)))
            res += (len(string) - len(new_string))
            func(p + 1, new_string)
    func(0, s)
    return res


if __name__ == "__main__":
    arr = [i + 1 for i in range(6)]
    print(arr)
    # print(bisect.bisect_left(arr, 3))
    print(bisect.bisect_left(arr, 6))
    # print(arr)

    nums = [1, 3, 2, 2, 3, 1]
    print([(j, i) for i, j in collections.Counter(nums).most_common()])

    arr = [[1,2,3], [4,5]]
    for i, j in zip(*arr):
        print(i, j)
    
    print(total_prefix('abcabcd'))

    dq = collections.deque(nums)
    print(dq)
    del dq[3]
    print(dq)

    count = 0
    while count <= 5:
        print('In while loop: ', count)
        count += 1
        if count == 3:
            break
    else:
        print('More than 5')
