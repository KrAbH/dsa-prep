# https://cses.fi/problemset/task/1097

import sys
sys.setrecursionlimit(10**7)
class Solution:
    def __init__(self, n, values):
        self.n = n
        self.values = [0] + values
        self.prefix = self.get_prefix(values)
        self.mem = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def get_prefix(self, values):
        prefix = [0]
        for v in values:
            prefix.append(prefix[-1] + v)
        return prefix
    
    def get_interval_sum(self, i, j):
        return self.prefix[j] - self.prefix[i-1]

    def removal_game(self, i, j):
        if i == j:
            return self.values[i]
        if self.mem[i][j] != -1:
            return self.mem[i][j]
        mx = float("-inf")
        if i+1 <= j:
            mx = max(mx, self.values[i] + self.get_interval_sum(i+1, j) - self.removal_game(i+1, j))
        if i <= j-1:
            mx = max(mx, self.values[j] + self.get_interval_sum(i, j-1) - self.removal_game(i, j-1))
        
        self.mem[i][j] = mx
        return mx



if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    solver = Solution(n, values)
    print(solver.removal_game(1, n))
    