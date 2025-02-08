# https://cses.fi/problemset/task/1745
# topics: dynamic programming, knapsack
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def __init__(self, n, coins):
        self.n = n
        self.coins = coins
        self.mem = [[-1 for _ in range(10**5 + 1)] for _ in range(n)]
    
    def money_sums(self, i, total):
        if i == self.n:
            return set([total])
        if type(self.mem[i][total]) != type(1):
            return self.mem[i][total]
        ans = set()
        ans |= self.money_sums(i+1, total)
        ans |= self.money_sums(i+1, total + self.coins[i])
        self.mem[i][total] = ans
        return ans
    
    def money_sums_tab(self):
        dp = [[set() for _ in range(2*10**5 + 1)] for _ in range(self.n + 1)]
        for i in range(self.n, -1, -1):
            for j in range(10**5 + 1):
                if i == self.n:
                    dp[i][j].add(j)
                else:
                    dp[i][j] |= dp[i+1][j]
                    dp[i][j] |= dp[i+1][j + self.coins[i]]

        return dp[0][0]
        
if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    solver = Solution(n, values)
    # ans = solver.money_sums(0, 0)
    ans = solver.money_sums_tab()
    ans = list(ans)
    ans.sort()
    ans = ans[1:]
    print(len(ans))
    print(" ".join(map(str, ans)))