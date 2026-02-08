t = int(input().strip())

for _ in range(t):
    s = input().strip()
    n = len(s)
    found = False

    for i in range(1, n):
        a = s[:i]
        b = s[i:]

        if (len(a) > 1 and a[0] == "0") or (len(b) > 1 and b[0] == "0"):
            continue

        a_val = int(a)
        b_val = int(b)

        if a_val > 0 and b_val > 0 and b_val > a_val:
            print(a_val, b_val)
            found = True
            break
    if not found:
        print(-1)