t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    # Check all fixed relevant patterns
    if "aa" in s:
        ans = min(ans, 2)
    if "aba" in s or "aca" in s:
        ans = min(ans, 3)
    if "abca" in s or "acba" in s:
        ans = min(ans, 4)
    if "abbacca" in s or "accabba" in s:
        ans = min(ans, 7)

    print(ans if ans != float('inf') else -1)