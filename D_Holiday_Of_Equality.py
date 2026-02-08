n = int(input().strip())
money = list(map(int, input().split()))
max_money = max(money)
total = 0

for m in money:
    total += max_money - m
print(total)