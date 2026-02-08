n = int(input().strip())
rating = list(map(int, input().split()))

rank = [-1] * n
pairs = [(r, i) for i, r in enumerate(rating)]
pairs.sort(reverse=True)

count = 1
seen = {}

for r, i in pairs:
    if r in seen:
        rank[i] = seen[r]  # same rank as previous if tie
    else:
        rank[i] = count
        seen[r] = count
    count += 1

print(*rank)
