import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    a = list(map(int, input_data[2:2+n]))
    b = list(map(int, input_data[2+n:2+n+m]))
    
    res = []
    i = 0
    
    for j in range(m):
        while i < n and a[i] < b[j]:
            i += 1
        res.append(i)
    print(*(res))

if __name__ == "__main__":
    solve()