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

if __name__ == "__main__":
    dq = collections.deque()
    dq.append(5)
    dq.appendleft(2)
    print(dq)
    print(len(dq))

    f = lambda x=0, y=0: (x+y) /2
    print(f())
