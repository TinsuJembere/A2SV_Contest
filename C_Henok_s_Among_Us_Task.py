a, b = map(int, input().split())

path = []

while b >= a:
    path.append(b)

    if b == a:
        path.reverse()
        print("YES")
        print(len(path))
        print(*path)
        exit()
    if b % 10 == 1:
        b = (b - 1) // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        break
print("NO")