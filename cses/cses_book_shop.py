import sys
# sys.setrecursionlimit(10**9)
class Solution:
    def __init__(self, n, amount_left, prices, pages):
        self.n = n
        self.amount_left = amount_left
        self.prices = prices
        self.pages = pages
        self.mem = [[-1 for _ in range(amount_left + 1)] for _ in range(n)]
    
    def solve(self, i, amount_left):
        if i == self.n:
            return 0
        if self.mem[i][amount_left] != -1:
            return self.mem[i][amount_left]
        mx_pages= 0
        mx_pages = max(mx_pages, self.solve(i+1, amount_left))
        if amount_left >= self.prices[i]:
            mx_pages = max(mx_pages, self.pages[i] + self.solve(i+1, amount_left - self.prices[i]))
        self.mem[i][amount_left] = mx_pages
        return self.mem[i][amount_left]
    
class SolutionTabulation:
    def __init__(self, n, amount_left, prices, pages):
        self.n = n
        self.amount_left = amount_left
        self.prices = prices
        self.pages = pages
        # self.mem = [[0 for _ in range(amount_left + 1)] for _ in range(n)]
        self.mem = [[]]
    
    def solve(self):
        for i in range(self.n):
            
            for j in range(self.amount_left + 1):
                without = self.mem[i-1][j] if i > 0 else 0
                selected = 0
                if j - self.prices[i] >= 0:
                    temp = 0
                    if i > 0 :
                        temp = max(temp, self.mem[i-1][j - self.prices[i]])
                    selected = self.pages[i] + temp 
                # selected = self.pages[i] + self.mem[i-1][j - self.prices[i]] if i > 0 and j - self.prices[i] >= 0 else 0
                self.mem[i][j] = max(self.mem[i][j], without, selected)
        
        return self.mem[n-1][amount_left]        
    
    #after making the observation that the computation of current state only depend on previous state, hence no need to maintain the whole matrix
    def solve_space_optimization(self):
        prev = [0]*(self.amount_left + 1)
        for i in range(self.n):
            curr = [0]*(self.amount_left + 1)
            for j in range(self.amount_left + 1):
                without = prev[j]
                selected = 0
                if j - self.prices[i] >= 0:
                    selected = self.pages[i] + prev[j - self.prices[i]] 
                # selected = self.pages[i] + self.mem[i-1][j - self.prices[i]] if i > 0 and j - self.prices[i] >= 0 else 0
                curr[j] = max(without, selected)
            prev = curr[:]
        
        return curr[amount_left]
if __name__ == "__main__":
    n, amount_left = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))
    # solver = Solution(n, amount_left, prices, pages)
    # print(solver.solve(0, amount_left))
    solver = SolutionTabulation(n, amount_left, prices, pages)
    print(solver.solve_space_optimization())
    

