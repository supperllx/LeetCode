from typing import Tuple, List
from math import log
import collections

# rates = [
#     [1, 0.23, 0.25, 16.43, 18.21, 4.94],
#     [4.34, 1, 1.11, 71.40, 79.09, 21.44],
#     [3.93, 0.90, 1, 64.52, 71.48, 19.37],
#     [0.061, 0.014, 0.015, 1, 1.11, 0.30],
#     [0.055, 0.013, 0.014, 0.90, 1, 0.27],
#     [0.20, 0.047, 0.052, 3.33, 3.69, 1],
# ]
# currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

rates = [
    [0, 0.7, 0],
    [0, 0, 9.5],
    [0.16,0,0]
]
currencies = ('PLN', 'EUR', 'USD')


n = len(currencies)

path = [[None for _ in range(n)] for _ in range(n)]
dist = [[0 for _ in range(n)] for _ in range(n)]

def print_path(i, j):
    if path[i][j] == i:
        print(' ', i, end = '')
    elif path[i][j] == None:
        print('No path')
    else:
        print(' ', path[i][j], end = '')
        print_path(i, path[i][j])

def arbitrage(currency_tuple: tuple, rates_matrix: Tuple[Tuple[float, ...]]):
    for i in range(n):
        for j in range(n):
            dist[i][j] = rates[i][j]
            if rates[i][j] > 0:
                path[i][j] = i

    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if not (i == j == k):
                    if dist[i][j] < dist[i][k] * dist[k][j]:
                        dist[i][j] = dist[i][k] * dist[k][j]
                        path[i][j] = path[k][j]
    
    for i in range(n):
        if dist[i][i] > 1:
            print('arbitrage: ', currencies[i], ' ', dist[i][i])
            print_path(i, i)
            print()
            print('---')
    



if __name__ == "__main__":
    arbitrage(currencies, rates)

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)