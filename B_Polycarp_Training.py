n = int(input().strip())
a = list(map(int, input().split()))

a.sort()
days = 1
for problem in a:
    if problem >= days:
        days += 1
print(days - 1)