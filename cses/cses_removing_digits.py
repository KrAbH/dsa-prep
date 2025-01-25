import sys
sys.setrecursionlimit(10**8)

class Solver:
    def __init__(self, n):
        self.n = n
        self.mem = [-1 for _ in range(n+1)]

    def extract_options(self, n):
        s = set()
        while n:
            rem = n%10
            n = n // 10
            s.add(int(rem))
        return s
    
    def minimize_steps(self, n):
        if n == 0:
            return 0
        if self.mem[n] != -1:
            return self.mem[n]
        mn = float("inf")
        options = self.extract_options(n)
        for option in options:
            if n - option >= 0 and option > 0:
                mn = min(mn, 1 + self.minimize_steps(n - option))
        self.mem[n] = mn
        return self.mem[n]
        
if __name__ == "__main__":
    n = int(input())
    solver  = Solver(n)
    print(solver.minimize_steps(n))
