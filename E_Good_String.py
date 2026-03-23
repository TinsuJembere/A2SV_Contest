n = int(input())
s = input().strip()

res = []

for c in s:
    if len(res) % 2 == 0:
        res.append(c)
    else:
        if res[-1] != c:
            res.append(c)

if len(res) % 2 == 1:
    res.pop()

print(n - len(res))
print("".join(res))