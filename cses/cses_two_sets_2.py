# https://cses.fi/problemset/task/1093
#getting wrong answer for few test cases, need to debug

class Solution:
    def __init__(self, n):
        self.n = n
    
    def count_two_sets(self):
        total = self.n * (self.n + 1) // 2
        if total & 1 == 1:
            return 0
        tab = [[0 for _ in range(total+1 )] for _ in range(self.n + 2)]
        tab[self.n + 1][total//2] = 1
        for i in range(self.n, 0 , -1):
            for j in range(total+1):
                tab[i][j] = tab[i+1][j] + tab[i+1][j+ i ] if j + i <= total else tab[i+1][j]
                # tab[i][j] %= 10**9 + 7
        return tab[1][0]
    
if __name__ == "__main__":
    n = int(input())
    solver = Solution(n)
    print(solver.count_two_sets()//2)