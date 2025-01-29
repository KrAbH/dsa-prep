import sys
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#we only need to check with previous number, not necessarily both adjacent numbers
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

    def count_arr_1(self, idx, prev):
        # print(idx, prev)
        if idx == self.n:
            return 1
        if self.mem[idx][prev] != -1:
            return self.mem[idx][prev]
        count = 0
        if self.arr[idx] > 0:
            if abs(self.arr[idx] - prev) <= 1:
                count = self.count_arr_1(idx +1, self.arr[idx])
                count %= mod
        else:
            if prev > 0:
                candidates = [prev]
                if prev -1 > 0:
                    candidates.append(prev -1)
                if prev + 1<= self.m:
                    candidates.append(prev + 1)
            else:
                candidates = [i for i in range(1, self.m + 1)]
            for candidate in candidates:
                count += self.count_arr_1(idx +1, candidate)
                count %= mod

        self.mem[idx][prev] = count
        return count 

    def tabulation_solution(self):
        dp = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]
        for i in range(n, -1, -1):
            for last_num in range(1, self.m + 1):
                if i == self.n:
                    dp[i][last_num] = 1
                else:
                    if self.arr[i] > 0:
                        if abs(last_num - self.arr[i]) <=1:
                            dp[i][last_num] = dp[i+1][self.arr[i]]
                    else:
                        for diff in [0, 1, -1]:
                            curr = last_num + diff
                            if 1 <= curr <= m:
                                dp[i][last_num] += dp[i+1][curr]
                dp[i][last_num] %= mod
        ans = 0
        # print(dp)
        if self.arr[0] > 0:
            return dp[1][self.arr[0]]
        else:
            for i in range(1, m+1):
                ans += dp[1][i]
                ans %= mod
        return ans
    
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    solver = Solution(n, m, arr)
    # ans = solver.count_arr_1(0, arr[0])
    ans = solver.tabulation_solution()
    # print(solver.mem)
    print(ans)

