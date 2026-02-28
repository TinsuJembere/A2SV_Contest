from collections import Counter

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    freq = Counter(s)
    alphabets = len(freq)
    if alphabets == 1:
        print("NO")
        continue
    if alphabets == 2:
        values = list(freq.values())
        if 1 in values:
            print("NO")
            continue
    print("YES")