import collections

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
