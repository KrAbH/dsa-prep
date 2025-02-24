# https://cses.fi/problemset/task/1140

import sys
sys.setrecursionlimit(10**7)
class Solution:
    def __init__(self, n, info):
        self.n = n
        self.info = info
        self.info.sort()
        self.mem = [-1 for _ in range(self.n)]

    def bs(self, i, point):
        lo, hi = i, self.n-1
        ans = self.n
        while(lo <= hi):
            mid = (lo + hi)//2
            if self.info[mid][0] > point:
                ans = mid
                hi = mid -1
            else:
                lo = mid +1
        return ans

    # instead of maintaing the last ending time which we are using the ending time to trim our choices, of which intervals are possible when we choose it.
    def projects_mem(self, i):
        if i == self.n:
            return 0
        if self.mem[i] != -1:
            return self.mem[i]
        mx = float("-inf")
        choices = self.bs(i +1, self.info[i][1])
        # print(i)
        # print(choices)
        # print("Transitions")
        for choice in range(choices, self.n+1):
            mx = max(mx, self.info[i][2] + self.projects_mem(choice))
        mx = max(mx, self.projects_mem(i+1))
        self.mem[i] = mx
        return self.mem[i]
    
    def projects_tab_memory_heavy(self):
        self.info.sort()
        # for i in self.info:
        #     print(i)
        dp = [[0 for _ in range(self.info[-1][1] + 1)] for _ in range(self.n + 1)]
        
        for i in range(self.n, -1, -1):
            for j in range(self.info[-1][1] + 1):
                if i == self.n:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j]
                    if self.info[i][0] > j:
                        dp[i][j] = max(dp[i][j], self.info[i][2] + dp[i+1][self.info[i][1]])
        # print(dp)
        return dp[0][0]
    
    def projects_tab(self):
        tab = [0 for _ in range(self.n + 1)]
        for i in range(self.n - 1, -1, -1):
            # not taking
            tab[i] = max(tab[i], tab[i+1])
            # taking
            choices = self.bs(i+1, self.info[i][1])
            tab[i] = max(tab[i], self.info[i][2] + tab[choices])
        return tab[0]
                
if __name__ == "__main__":
    n = int(input())
    info = []
    for i in range(n):
        s = tuple(map(int, input().split()))
        info.append(s)
    # print(info)
    solver = Solution(n, info)
    # print(solver.projects_tab())
    
    # print(solver.projects_mem(0))
    print(solver.projects_tab())
