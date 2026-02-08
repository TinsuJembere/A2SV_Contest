n = int(input().strip())
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
rank = {}
current_rank = 1

for i in range(n):
    if sorted_a[i] not in rank:
        rank[sorted_a[i]] = current_rank
    current_rank += 1
for x in a:
    print(rank[x], end=" ")
    