import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

left = [0]*n
stack = []
cur_sum = 0

for i in range(n):
    cnt = 1
    while stack and stack[-1][0] > m[i]:
        h, c = stack.pop()
        cur_sum -= h * c
        cnt += c
    stack.append((m[i], cnt))
    cur_sum += m[i] * cnt
    left[i] = cur_sum

right = [0]*n
stack = []
cur_sum = 0

for i in range(n-1, -1, -1):
    cnt = 1
    while stack and stack[-1][0] > m[i]:
        h, c = stack.pop()
        cur_sum -= h * c
        cnt += c
    stack.append((m[i], cnt))
    cur_sum += m[i] * cnt
    right[i] = cur_sum

best = 0
peak = 0

for i in range(n):
    total = left[i] + right[i] - m[i]
    if total > best:
        best = total
        peak = i

a = [0]*n
a[peak] = m[peak]

for i in range(peak-1, -1, -1):
    a[i] = min(m[i], a[i+1])

for i in range(peak+1, n):
    a[i] = min(m[i], a[i-1])

print(*a)