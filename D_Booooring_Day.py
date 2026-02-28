t = int(input().strip())

for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    win = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += a[right]
        while current_sum > r and l <= r:
            current_sum -= a[left]
            left += 1
        if current_sum >= l and current_sum <= r:
            current_sum = 0
            win += 1
            left = right + 1
    print(win)