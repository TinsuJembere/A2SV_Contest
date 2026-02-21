n = int(input().strip())
w, h = map(int, input().split())

prev = max(w, h)
possible = True

for i in range(n - 1):
    w, h = map(int, input().split())
    big = max(w, h)
    small = min(w, h)

    if big <= prev:
        prev = big
    elif small <= prev:
        prev = small
    else:
        possible = False
print("YES" if possible == True else "NO")