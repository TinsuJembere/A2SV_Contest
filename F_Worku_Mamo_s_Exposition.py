from collections import deque

n, k = map(int, input().split())
h = list(map(int, input().split()))

max_d = deque()
min_d = deque()

l = 0
max_len = 0
segments = []

for r in range(n):
    while max_d and h[max_d[-1]] <= h[r]:
        max_d.pop()
    max_d.append(r)

    while min_d and h[min_d[-1]] >= h[r]:
        min_d.pop()
    min_d.append(r)

    while h[max_d[0]] - h[min_d[0]] > k:
        if max_d[0] == l:
            max_d.popleft()
        if min_d[0] == l:
            min_d.popleft()
        l += 1

    length = r - l + 1

    if length > max_len:
        max_len = length
        segments = [(l + 1, r + 1)]
    elif length == max_len:
        segments.append((l + 1, r + 1))

print(max_len, len(segments))
for seg in segments:
    print(seg[0], seg[1])