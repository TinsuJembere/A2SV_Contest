n, k = map(int, input().split())
road = input().strip()
current = 0
max_block = 0

for c in road:
    if c == '#':
        current += 1
        max_block = max(max_block, current)
    else:
        current = 0
    
if max_block >= k:
    print("NO")
else:
    print("YES")
    