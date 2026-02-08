q = int(input())

for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1

    if i != len(s):
        print("NO")
        continue

    from collections import Counter
    need = Counter(t) - Counter(s)
    have = Counter(p)

    possible = True
    for ch in need:
        if need[ch] > have[ch]:
            possible = False
            break

    print("YES" if possible else "NO")