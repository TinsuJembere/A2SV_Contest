n, m = map(int, input().split())

total = 0
saving = []

for _ in range(n):
    a, b = map(int, input().split())
    total += a
    saving.append(a - b)
if total <= m:
    print(0)
else:
    saving.sort(reverse=True)
    count = 0

    for s in saving:
        total -= s
        count += 1

        if total <= m:
            print(count)
            break
    else:
        print(-1)
