# https://cses.fi/problemset/task/1097
# similar problem for above is https://atcoder.jp/contests/dp/tasks/dp_l , it has similar transition function. Focus on the function's definition for designing the transition.
# solution https://www.youtube.com/watch?v=luyErUWATsY&t=2137s 

import sys
sys.setrecursionlimit(10**7)
class Solution:
    def __init__(self, n, values):
        self.n = n
        self.values = values
        self.prefix = self.get_prefix(values)
        self.mem = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def get_prefix(self, values):
        prefix = []
        s = 0
        for v in values:
            s += v
            prefix.append(s)
        return prefix
    
    def get_interval_sum(self, i, j):
        if i-1 >= 0:
            return self.prefix[j] - self.prefix[i-1]
        else:
            return self.prefix[j]

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
    
    def removal_sum_tab(self):
        tab = [[float("-inf") for _ in range(self.n)]for _ in range(self.n)]
        for diff in range(n):
            for i in range(n):
                l, r = i, i + diff
                if r <= n-1:
                    if l == r:
                        tab[l][r] = self.values[l]
                    else:
                        tab[l][r] = max(tab[l][r], self.values[l] + self.get_interval_sum(l+1, r) - tab[l+1][r])
                        tab[l][r] = max(tab[l][r], self.values[r] + self.get_interval_sum(l, r-1) - tab[l][r - 1])
        # print(tab)
        return tab[0][self.n - 1]
    

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    solver = Solution(n, values)
    # print(solver.removal_game(1, n))
    print(solver.removal_sum_tab())
    