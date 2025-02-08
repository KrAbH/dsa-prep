# https://cses.fi/problemset/task/1140

import sys
sys.setrecursionlimit(10**7)
class Solution:
    def __init__(self, n, info):
        self.n = n
        self.info = info
    
    def projects_tab(self):
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

if __name__ == "__main__":
    n = int(input())
    info = []
    for i in range(n):
        s = tuple(map(int, input().split()))
        info.append(s)
    # print(info)
    solver = Solution(n, info)
    print(solver.projects_tab())
