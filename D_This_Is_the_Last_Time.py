import sys
input = sys.stdin.read
data = input().strip().split()

idx = 0
t = int(data[idx])
idx += 1

answers = []

for _ in range(t):
    n = int(data[idx])
    k = int(data[idx + 1])
    idx += 2
    
    casinos = []
    
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx + 1])
        real = int(data[idx + 2])
        idx += 3
        
        # store as (real, l, r)
        casinos.append((real, l, r))
    
    # sort by resulting coins
    casinos.sort()
    
    coins = k
    
    for real, l, r in casinos:
        if l <= coins <= r and real > coins:
            coins = real
    
    answers.append(str(coins))

print("\n".join(answers))