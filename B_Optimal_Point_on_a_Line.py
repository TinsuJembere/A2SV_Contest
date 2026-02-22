n = int(input().strip())
x = list(map(int, input().split()))
x.sort()
print(x[(n - 1) // 2])