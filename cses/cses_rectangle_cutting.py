import sys
sys.setrecursionlimit(10**8)

class Solver():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mem = [[[[-1 for _ in range(self.m + 1)] for _ in range(self.m + 1)]for _ in range(self.n + 1)] for _ in range(self.n + 1)]

    def min_rect_cut_mem(self, x_s, x_e, y_s, y_e):
        if x_e - x_s == y_e - y_s:
            return 0
        
        if self.mem[x_s][x_e][y_s][y_e] != -1:
            return self.mem[x_s][x_e][y_s][y_e]
        mn = float("inf")
        for x in range(x_s + 1, x_e):
            tmp = 1+ self.min_rect_cut_mem(x_s, x, y_s, y_e) + self.min_rect_cut_mem(x, x_e, y_s, y_e)
            mn = min(mn, tmp)
        for y in range(y_s + 1, y_e):
            tmp = 1+ self.min_rect_cut_mem(x_s, x_e, y_s, y) + self.min_rect_cut_mem(x_s, x_e, y, y_e)
            mn = min(mn, tmp)
        # mn += 1
        self.mem[x_s][x_e][y_s][y_e] = mn
        return self.mem[x_s][x_e][y_s][y_e]
if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    solver = Solver(a, b)
    print(solver.min_rect_cut_mem(0, a, 0, b))