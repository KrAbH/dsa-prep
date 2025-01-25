# https://cses.fi/problemset/task/1634
import sys
sys.setrecursionlimit(10**7)

class Solver:
    def __init__(self, x, coins):
        self.x = x
        self.coins = coins
        self.mem = [-1 for _ in range(x+1)]
    
    def minimize_coins(self, x):
        if x == 0:
            self.mem[x] = 0
            return 0
        if self.mem[x] != -1:
            return self.mem[x]
        min_coins = float("inf")
        for coin in coins:
            if x - coin >= 0:
                min_coins = min(min_coins, 1 + self.minimize_coins(x - coin))
        self.mem[x] = min_coins
        return self.mem[x]

class Solver_Tab:
    def __init__(self, x, coins):
        self.x = x
        self.coins = coins
        self.mem = [float("inf") for _ in range(x+1)]
        self.mem[0] = 0

    def minimize_coins(self, x):
        for i in range(1, x+1):
            mn = float("inf")
            for coin in self.coins:
                if i - coin >= 0:
                    mn = min(mn, 1 + self.mem[i- coin])
            self.mem[i] = mn
        return self.mem[x]
    
if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    solver = Solver(x,coins)
    ans = solver.minimize_coins(x)
    print(solver.mem)
    if ans == float("inf"):
        print("-1")
    else:
        print(ans)
