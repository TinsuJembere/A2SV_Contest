def winner(p, q):
    while True:
        if p*3 == 2*q:
            return "Bob"
        if p == 0 or q == 1:
            return "Alice"
        if p*3 > 2*q:
            # Alice can decrease q to avoid 2/3
            return "Alice"
        # Bob's move: decrease p
        # Simulate optimal moves with reduction
        k = (2*q - 3*p) // 3
        if k == 0:
            # cannot avoid
            return "Bob"
        # reduce q by k
        q -= k
