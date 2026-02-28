n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
max_length = 0
my_sum = 0

for r in range(n):
    my_sum += arr[r]
    
    while my_sum > s:
        my_sum -= arr[l]
        l += 1

    if my_sum <= s:
        current_length = r - l + 1
        max_length = max(max_length, current_length)

print(max_length)