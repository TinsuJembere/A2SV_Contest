t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    nums = list(map(int, input().split()))
    nums.sort()
    score = 0
    for i in range(0, 2 * n, 2):
        score += nums[i]
    print(score)