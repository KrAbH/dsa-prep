import sys
sys.setrecursionlimit(10**7)

class Solver:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.n = len(str1)
        self.m = len(str2)
        self.mem = [[-1 for _ in range(self.m + 1)] for _ in range(self.n+1)]

    def edit_distance_rec(self, i, j):
        if i == self.n or j == self.m:
            return (self.n - i) + (self.m - j)
        if self.mem[i][j] != -1:
            return self.mem[i][j]
        
        ans = float("inf")
        if self.str1[i] != self.str2[j]:
            ans = 1+  min(self.edit_distance_rec(i+1, j), self.edit_distance_rec(i, j+1), self.edit_distance_rec(i+1, j+1))
        else:
            ans = self.edit_distance_rec(i+1, j+1)
        self.mem[i][j] = ans
        return ans
    
    def edit_distance_tab(self):

        for i in range(self.n, -1, -1):
            for j in range(self.m, -1, -1):
                # print(i, j)
                if i == self.n or j == self.m:
                    self.mem[i][j] = (self.n - i) + (self.m - j)
                else:
                    if self.str1[i] == self.str2[j]:
                        self.mem[i][j] = self.mem[i+1][j+1]
                    else:
                        self.mem[i][j] = 1 + min(self.mem[i+1][j], self.mem[i][j+1], self.mem[i+1][j+1])
        
        return self.mem[0][0]

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    sovler = Solver(str1, str2)
    print(sovler.edit_distance_tab())