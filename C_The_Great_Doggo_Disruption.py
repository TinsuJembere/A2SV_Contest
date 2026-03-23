import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

from collections import Counter

freq = Counter(s)

if n > 1 and max(freq.values()) == 1:
    print("No")
else:
    print("Yes")