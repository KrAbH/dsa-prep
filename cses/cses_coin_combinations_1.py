# https://cses.fi/problemset/task/1635
import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7

class Solver:
    def __init__(self, x, coins):
        self.x = x
        self.coins = coins
        self.mem = [-1 for _ in range(x + 1)]

    def count_coin_combinations(self, amount):
        if amount == 0:
            self.mem[amount] = 1
            return self.mem[amount]
        if self.mem[amount] != -1:
            return self.mem[amount]
        count  = 0
        for coin in self.coins:
            rem_amount = amount - coin
            if rem_amount >=0:
                count += self.count_coin_combinations(rem_amount)
                count %= mod
        self.mem[amount] = count
        return count
    
    def tabular_solution(self):
        mem = [0]*(self.x+1)
        for i in range(0, self.x+1):
            if i ==0:
                mem[i] = 1
            else:
                for coin in self.coins:
                    if i - coin >= 0:
                        mem[i] += mem[i - coin]
                        mem[i] %= mod
        return mem[self.x]%mod
    
if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    solver = Solver(x, coins)
    # ans = solver.count_coin_combinations(x)
    ans = solver.tabular_solution()
    print(ans)