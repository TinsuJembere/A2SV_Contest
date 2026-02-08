target =int(input().strip())
for i in range(target):
    a, b, c = map(int, input().split())
    if a + b - c == 0:
        print("YES")
    elif a + c - b == 0:
        print("YES")
    elif b + c - a == 0:
        print("YES")
    else:
        print("NO")