import sys
input = sys.stdin.read

data = input().strip().split()
n = int(data[0])

segments = []
idx = 1

for i in range(1, n + 1):
    l = int(data[idx])
    r = int(data[idx + 1])
    idx += 2
    segments.append((l, r, i))  

segments.sort(key=lambda x: (x[0], -x[1]))

max_right = -1
max_index = -1

for l, r, original_idx in segments:
    if r <= max_right:
        print(original_idx, max_index)
        sys.exit() 
    
    max_right = r
    max_index = original_idx

print(-1, -1)
