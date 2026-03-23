from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    brand_sum = defaultdict(int)

    for _ in range(k):
        b, c = map(int, input().split())
        brand_sum[b] += c

    print(sum(heapq.nlargest(n, brand_sum.values())))