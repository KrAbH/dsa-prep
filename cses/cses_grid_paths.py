#https://cses.fi/problemset/task/1638
import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
class Solver:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid
        self.mem = [[-1 for _ in range(n)] for _ in range(n)]
        self.directions = [[1, 0], [0, 1]]
    def count_paths(self, x, y):
        if grid[x][y] == '*':
            return 0
        if x == self.n -1 and y == self.n -1:
            if self.grid[x][y] == '.':
                return 1
            else:
                return 0
        if x >= self.n or y >= self.n:
            return 0
        if self.mem[x][y] != -1:
            return self.mem[x][y]
        count = 0
        for dx, dy in self.directions:
            i, j = x + dx, y + dy
            if 0 <= i < self.n and 0 <= j < self.n and self.grid[i][j] == '.':
                count += self.count_paths(i, j) 
                count %= mod
        self.mem[x][y] = count
        return self.mem[x][y]

if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())
    solver = Solver(n, grid)
    print(solver.count_paths(0, 0))
    
