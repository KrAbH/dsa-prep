import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
class Solution:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr
        self.mem = [[-1 for _ in range(m+1)] for _ in range(n)]
    
    def count_arr(self, i, last_num):
        if i == self.n:
            return 1
        if self.mem[i][last_num] != -1:
            return self.mem[i][last_num]
        
        count = 0
        if self.arr[i] > 0:
            if abs(self.arr[i] - last_num) <= 1:
                 count = self.count_arr(i+1, self.arr[i])
        else:
            
            if last_num == 0:
                candidates = [j for j in range(1, m+1)]
            else:
                candidates = [last_num]
                if last_num - 1 > 0:
                    candidates.append(last_num - 1)
                if last_num + 1 <= self.m:
                    candidates.append(last_num + 1)
            if i < self.n - 1:
                nxt = self.arr[i + 1]
                if nxt > 0:
                    for candidate in candidates:
                        if abs(nxt - candidate) <= 1:
                            count += self.count_arr(i+1, candidate)
                            count %= mod
                else:
                    for candidate in candidates:
                        count += self.count_arr(i+1, candidate)
                        count %= mod
            else:
                for candidate in candidates:
                        count += self.count_arr(i+1, candidate)
                        count %= mod
        self.mem[i][last_num] = count
        return count 
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    solver = Solution(n, m, arr)
    # if arr[0] > 0:
    #     ans += solver.count_arr(0, arr[0])
    # else:
    #     for i in range(1, m+1):
    #         ans += solver.count_arr(0, i)
    ans = solver.count_arr(0, arr[0])
    
    print(ans)

