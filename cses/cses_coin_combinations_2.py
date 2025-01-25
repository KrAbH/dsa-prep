# https://cses.fi/problemset/task/1635
import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7

class Solver:
    def __init__(self, n, x, coins):
        self.x = x
        self.n = n
        self.coins = coins
        self.mem = [[-1 for _ in range(n)]for _ in range(x + 1)]

    def count_coin_combinations(self, idx, amount):

        if amount == 0:
            # self.mem[amount][idx] = 1
            return 1
        if idx == self.n:
            return 0
        if self.mem[amount][idx] != -1:
            return self.mem[amount][idx]
        count  = 0
        count += self.count_coin_combinations(idx+1, amount)
        count %= mod
        rem_amount = amount - self.coins[idx]
        if rem_amount >= 0:
            count += self.count_coin_combinations(idx, rem_amount)
            count %= mod                
        self.mem[amount][idx] = count
        return count
    
if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    solver = Solver(n, x, coins)
    ans = solver.count_coin_combinations(0, x)
    print(ans)