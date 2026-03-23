import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = [list(map(int, input().split())) for _ in range(n)]
    
    if n == 1 and m == 1:
        print(-1)
        continue

    b = [[0]*m for _ in range(n)]

    if m > 1:
        # shift each row left
        for i in range(n):
            for j in range(m):
                b[i][j] = a[i][(j+1) % m]
    else:
        # shift column down
        for i in range(n):
            b[i][0] = a[(i+1) % n][0]

    for row in b:
        print(*row)