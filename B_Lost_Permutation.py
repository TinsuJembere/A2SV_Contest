t = int(input().strip())
for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))

    curr_sum = sum(b)
    total_sum = curr_sum + s
    n = max(b)
    possible = False

    while True:
        perm_sum = n * (n + 1) // 2
        if perm_sum == total_sum:
            possible = True
            break
        if perm_sum > total_sum:
            break
        n += 1
    print("YES" if possible else "NO")