import sys


input_data = sys.stdin.read().split()
n = int(input_data[0])
idx = 1
towers = []
all_blocks = []

for _ in range(n):
    k = int(input_data[idx])
    idx += 1
    current_tower = []
    for _ in range(k):
        val = int(input_data[idx])
        current_tower.append(val)
        all_blocks.append(val)
        idx += 1
    towers.append(current_tower)

sorted_blocks = sorted(all_blocks)
successor = {}
for i in range(len(sorted_blocks) - 1):
    successor[sorted_blocks[i]] = sorted_blocks[i+1]
    
splits = 0
for tower in towers:
    for i in range(len(tower) - 1):
        u = tower[i]
        v = tower[i+1]
        if u not in successor or successor[u] != v:
            splits += 1
            
total_segments = n + splits
combines = total_segments - 1

print(f"{splits} {combines}")
