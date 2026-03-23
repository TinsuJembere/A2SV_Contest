n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l1, l2 = 0, 0
res = []
while l1 < n and l2 < m:
    if a[l1] < b[l2]:
        res.append(a[l1])
        l1 += 1
    else:
        res.append(b[l2])
        l2 += 1
res.extend(a[l1:])
res.extend(b[l2:])

print(*res)