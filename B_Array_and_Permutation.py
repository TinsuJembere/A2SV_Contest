t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    pos = 0  # pointer on p
    possible = True
    i = 0
    while i < n:
        # current value to match
        val = a[i]
        # find this val in p starting from pos
        while pos < n and p[pos] != val:
            pos += 1
        if pos == n:
            possible = False
            break
        # consume consecutive same values in a
        while i < n and a[i] == val:
            i += 1
        pos += 1  # move past the matched value in p
    print("YES" if possible else "NO")
