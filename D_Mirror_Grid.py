t = int(input().strip())
for _ in range(t):
    n = int(input())
    grid = [map(int, (input().strip())) for _ in range(n)]
    operations = 0

    for i in range(n // 2):
        for j in range(n):
            a = grid[i][j]
            b = grid[j][n - 1 - i]
            c = grid[n - 1 - i][n - 1 - j]
            d = grid[n - 1 - j][i]

            ones = (a == '1') + (b == "1") + (c == "1") + (d == "1")
            operations += min(ones, 4 - ones)
    print(operations)