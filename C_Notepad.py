t = int(input().strip())
for _ in range(t):
    n = int(input())
    s = input()

    hmap = {}
    flag = False
    for i in range(n - 1):
        temp = s[i:i+ 2]
        if temp in hmap: 
            if i - hmap[temp] >= 2:
                flag = True
                break
        else:
            hmap[temp] = i
    print("YES" if flag else "NO")
