n, k = map(int, input().split())
s = input().strip()

s = sorted(s)
last = -1000
count = 0
total = 0

for c in s:
    val = ord(c) - ord("a") + 1

    if val >= last + 2:
        total += val
        last = val
        count += 1

    if count == k:
        break
if count < k:
    print(-1)
else:
    print(total)