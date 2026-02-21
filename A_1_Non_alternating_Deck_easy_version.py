t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    remaining = n
    alice = 0
    bob = 0
    step = 1
    while remaining > 0:
        take = min(step, remaining)
        if step == 1:
            alice += take
        else:
            block = (step - 2) // 2
            if block % 2 == 0:
                bob += take
            else:
                alice += take
        remaining -= take
        step += 1
    print(alice, bob)