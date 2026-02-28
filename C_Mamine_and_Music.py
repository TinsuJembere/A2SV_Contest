n, k = map(int, input().split())
a = list(map(int, input().split()))

instruments = [(a[i], i + 1) for i in range(n)]
instruments.sort()

total_days = 0
learned = []

for days, idx in instruments:
    if total_days + days <= k:
        learned.append(idx)
        total_days += days
    else:
        break
print(len(learned))
if(learned):
    print(*learned)