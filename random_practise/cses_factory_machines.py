#https://cses.fi/problemset/task/1620/
#topic: Binary Search 
#subtopic: BS on answer (Atomic contribution)

class Solver:
    def __init__(self, n, t, times):
        self.num_machines = n
        self.products_to_be_made = t
        self.time_required_by_machines = times
    
    def check(self, cutoff_time):
        total_created_products = 0 
        for time_required in self.time_required_by_machines:
            total_created_products += cutoff_time//time_required 
        return total_created_products >= self.products_to_be_made

    def shortest_time(self):
        lo, hi = 1, 10**18
        ans = hi
        while(hi >= lo):
            mid = (lo + hi)//2
            if self.check(mid):
                ans = mid
                hi = mid -1
            else:
                lo = mid +1
        return ans
 
if __name__ == '__main__':
    n, t = list(map(int, input().split()))
    time = list(map(int, input().split()))
    solver = Solver(n, t, time)
    ans = solver.shortest_time()
    print(ans)

