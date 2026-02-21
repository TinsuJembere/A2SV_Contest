t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    remaining = n
    aw = 0
    ab = 0

    bw = 0
    bb = 0
    step = 1
    pos = 1
    while remaining > 0:
        take = min(step, remaining)
        if pos % 2 == 1:
            white = (take + 1) // 2
        else:
            white = take // 2
        black = take - white
        if step == 1:
            aw += white
            ab += black
        else:
            block = (step - 2) // 2
            if block % 2 == 0:
                bw += white
                bb += black
            else:
                ab += black
                aw += white
        remaining -= take
        step += 1
        pos += take
    print(aw, ab, bw, bb)