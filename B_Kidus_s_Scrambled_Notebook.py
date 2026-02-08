t = int(input().strip())

for j in range(t):
    num = input().strip()
    n = len(num)
    for i in range(1, n):
        prefix = num[:i]
        suffix = num[i:]

        if prefix[0] == "0" or suffix[0] == "0":
            continue
        if int(prefix) < int(suffix):
            print(f"{prefix} {suffix}")
            break

    else:
        print(-1)