n = int(input().strip())
towers = []
all_blocks = []

for _ in range(n):
    curr_tower = []
    data = list(map(int, input().split()))
    k = data[0]
    block = data[1:]
    towers.append(block)
    all_blocks.extend(block)
sorted_block = sorted(all_blocks)
successor = {}
for i in range(len(sorted_block) - 1):
    successor[sorted_block[i]] = sorted_block[i + 1]

split = 0
for tower in towers:
    for i in range(len(tower) - 1):
        u = tower[i]
        v = tower[i + 1]

        if u not in successor or successor[u] != v:
            split += 1
total_segments = n + split
combine = total_segments - 1
print(split, combine)
