# https://cses.fi/problemset/task/1633
import sys
sys.setrecursionlimit(10**7)
mod = 10**9 + 7
class Solver:
    def __init__(self, n):
        self.n = n
        self.mem = [-1 for _ in range(n+1)]
    
    def solve(self, n):
        if n == 0:
            return 1
        if self.mem[n] != -1:
            return self.mem[n]
        count = 0
        for i in range(1, 7):
            if n - i >= 0:
                count += self.solve(n - i)
                count %= mod
        self.mem[n] = count
        return self.mem[n]

class Solver_tab:
    def __init__(self, n):
        self.n = n
        self.tab = [0 for _ in range(n+1)]
        self.tab[0] = 1
    def solve(self):
        for i in range(1, self.n + 1):
            for j in range(1, 7):
                if i - j >= 0:
                    self.tab[i] += self.tab[i-j]
                    self.tab[i] = self.tab[i] % mod
        return self.tab[self.n]
        

if __name__ == "__main__":
    n = int(input())
    solver = Solver_tab(n)
    # print(solver.solve(n))
    print(solver.solve())