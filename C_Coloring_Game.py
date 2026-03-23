import sys
input = sys.stdin.readline

def count_pairs_greater(arr, right, T):
    count = 0
    left = 0
    
    while left < right:
        if arr[left] + arr[right] > T:
            count += right - left
            right -= 1
        else:
            left += 1
            
    return count

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    ans = 0
    mx = nums[-1]

    for k in range(2, n):
        T = max(nums[k], mx - nums[k])
        ans += count_pairs_greater(nums, k-1, T)

    print(ans)

t = int(input())
for _ in range(t):
    solve()