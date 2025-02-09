import sys
sys.setrecursionlimit(10**8)

class Solver():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mem = [[[[-1 for _ in range(self.m + 1)] for _ in range(self.m + 1)]for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        self.dp = [[-1 for _ in range(self.m + 1)] for _ in range(self.n + 1)]

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
    def min_rect_cut_mem_v2(self, x, y):
        # print(x, y)
        if x == y:
            return 0
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        mn = float("inf")
        for i in range(1, x):
            mn = min(mn, self.min_rect_cut_mem_v2(i, y) + self.min_rect_cut_mem_v2(x - i, y) + 1)
        
        for i in range(1, y):
            mn = min(mn, self.min_rect_cut_mem_v2(x, i) + self.min_rect_cut_mem_v2(x, y - i) + 1)

        self.dp[x][y] = mn
        return mn
    
    def min_rect_cut_tab(self):
        tab = [[float("inf") for _ in range(self.m + 1)] for _ in range(self.n + 1)]
        for x in range(1, self.n +1):
            for y in range(1, self.m + 1):
                if x == y:
                    tab[x][y] = 0
                else:
                    for i in range(1, x):
                        tab[x][y] = min(tab[x][y], 1 + tab[x-i][y] + tab[i][y])
                    for i in range(1, y):
                        tab[x][y] = min(tab[x][y], 1+ tab[x][y-i] + tab[x][i])
        return tab[self.n][self.m]
if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    solver = Solver(a, b)
    # print(solver.min_rect_cut_mem(0, a, 0, b))
    # print(solver.min_rect_cut_mem_v2(a, b))
    print(solver.min_rect_cut_tab())
    