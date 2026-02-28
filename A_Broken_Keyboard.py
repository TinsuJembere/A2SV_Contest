t = int(input().strip())

for _ in range(t):
    s = input().strip()

    i, n = 0, len(s)
    
    res = set()
    while i < n:
        j = i
        
        while j < n and s[i] == s[j]:
            j += 1
        length = j - i
        if length % 2 == 1:
            res.add(s[i])
        i = j
    print("".join(sorted(res)))