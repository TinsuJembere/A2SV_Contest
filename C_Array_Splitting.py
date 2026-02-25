import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:]))

    if k == 1:
        print(a[-1] - a[0])
        return

    gaps = []
    for i in range(n - 1):
        gaps.append(a[i+1] - a[i])
    gaps.sort(reverse=True)
    total_cost = a[-1] - a[0]

    for i in range(k - 1):
        total_cost -= gaps[i]

    print(total_cost)

if __name__ == "__main__":
    solve()