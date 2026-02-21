n = int(input().strip())
a = list(map(int, input().split()))

curr_sum = sum(a)
total_sum = n * (n + 1) // 2
print(total_sum - curr_sum)