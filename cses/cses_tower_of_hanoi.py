
def tower_of_hanoi(n, src, dest, aux):
    if n == 0:
        return []
    steps = []
    steps.extend(tower_of_hanoi(n-1, src, aux, dest))
    steps.append([src, dest])
    steps.extend(tower_of_hanoi(n-1, aux, dest, src))
    return steps
if __name__ == "__main__":
    n = int(input())
    ans = tower_of_hanoi(n, 1, 3, 2)
    print(len(ans))
    for step in ans:
        print(step[0], step[1])