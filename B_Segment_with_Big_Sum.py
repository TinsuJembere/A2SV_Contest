n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
min_length = float("inf")
my_sum = 0

for r in range(n):
    my_sum += arr[r]
    while my_sum >= s:
        current_length = r - l + 1
        min_length = min(min_length, current_length)
        my_sum -= arr[l]
        l += 1

print( -1 if min_length == float("inf") else min_length)