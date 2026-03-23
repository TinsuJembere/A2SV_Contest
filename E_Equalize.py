from collections import Counter

def max_equal_after_permutation(test_cases):
    results = []
    for n, a in test_cases:
        count = Counter()
        a_sorted = sorted(a)
        p_sorted = list(range(1, n + 1))
        for ai, pi in zip(a_sorted, reversed(p_sorted)):
            count[ai + pi] += 1
        results.append(max(count.values()))
    return results

t = int(input())  
test_cases = []

for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    test_cases.append((n, a))

results = max_equal_after_permutation(test_cases)
for res in results:
    print(res)