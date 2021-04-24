import collections
import sortedcontainers
def get_path(i, j, temp_path):
    if (i, j) not in path:
        print('No Path')
    elif path[(i, j)] == i:
        return temp_path + [i]
    else:
        return get_path(i, path[(i, j)], temp_path + [path[(i, j)]])


nodes = [('PLN', 'EUR', 0.7), ('EUR', 'USD', 9.5), ('USD', 'PLN', 0.16), ('CNY', 'USD', 0.15), ('USD', 'CNY', 7)]
# nodes = [('PLN', 'EUR', 0.7), ('EUR', 'USD', 9.5), ('USD', 'PLN', 0.16)]
# nodes = [['CNY', 'USD', 0.15], ['USD', 'CNY', 7]]

s = set()

graph = collections.defaultdict(int)
path = dict()
for u, v, w in nodes:
    graph[(u, v)] = w
    s.add(u)
    s.add(v)

s = list(s)
s.sort()

for c in s:
    graph[(c, c)] = 1

for u in s:
    for v in s:
        if (u, v) in graph:
            path[(u, v)] = v

for k in s:
    for i in s:
        for j in s:
            if (not i == k == j) and graph[(i, j)] < graph[(i, k)] * graph[(k, j)]:
                graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
                path[(i, j)] = path[(i, k)]

# for ik in range(len(s) - 1):
#     for iu in range(len(s)):
#         for iv in range(len(s)):
#             if graph[(s[iu], s[iv])] < graph[(s[iu], s[ik])] * graph[(s[ik], s[iv])]:
#                 graph[(s[iu], s[iv])] = graph[(s[iu], s[ik])] * graph[(s[ik], s[iv])]
#                 path[(s[iu], s[iv])] = path[(s[iu], s[ik])]

flag = False       
for c in s:
    if graph[(c, c)] > 1:
        print('arbitrage: ', graph[(c, c)])
        # print(get_path(c, c, [c])[::-1])
        flag = True
        start = c
        temp = []
        while c != path[(c, c)] and c not in temp:
            temp.append(c)
            c = path[(c, c)]
        print(temp + [start])

if not flag:
    print('No Way')

def dfs():
    s = set()
    graph = collections.defaultdict(list)
    for u, v, w in nodes:
        graph[u].append((v, w))
        s.add(u)
        s.add(v)
    max_profit = 1
    final_path = []

    visited = set()
    def func(cur, path, profit):
        nonlocal max_profit, final_path
        for nxt, v in graph[cur]:
            if nxt == start:
                if max_profit < profit * v:
                    max_profit = profit * v
                    final_path = path + [nxt]
            elif nxt not in visited:
                visited.add(nxt)
                func(nxt, path + [nxt], profit * v)
    for start in s:
        func(start, [start], 1)
        visited.clear()
    print('max: ', max_profit)
    print(final_path)

dfs()