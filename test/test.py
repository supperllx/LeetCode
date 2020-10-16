import collections
import heapq

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

if __name__ == "__main__":
    # dq = collections.deque()
    # dq.append(5)
    # dq.appendleft(2)
    # print(dq)
    # print(len(dq))

    # f = lambda x=0, y=0: (x+y) /2
    # print(f())

    print(coin(50))
    print(coin_2(50))

    dp = [[0 for i in range(7)] for j in range(3)]
    for i in range(7):
        dp[0][i] = 1
    for j in range(3):
        dp[j][0] = 1
    print(dp)

    print(frog([2, 3, 1, 1, 4]))
    print(frog([3,2,1,0,4]))

    array = [1] * 4096
    print(recursive_reduction(array, len(array)))

    cd = collections.Counter('abbc')
    cp = collections.Counter('bbcq')

    dd = collections.defaultdict(set)
    dd[5].add(1)
    print(dd[3])
    print(cd & cp)

    dq = collections.deque()
    dq += [1, 2, 3]
    print(dq)

    q = [(1, 100), (0, 120)]
    print(sorted(q))

    ct = collections.Counter({'a': -5, 'b': -3, 'c': -1})
    print(ct.most_common())