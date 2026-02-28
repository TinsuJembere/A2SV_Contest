import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        ops = []
        
        changed = True
        while changed:
            changed = False
            
            for i in range(n - 1):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    ops.append((1, i + 1))
                    changed = True
            
            for i in range(n - 1):
                if b[i] > b[i + 1]:
                    b[i], b[i + 1] = b[i + 1], b[i]
                    ops.append((2, i + 1))
                    changed = True
            
            for i in range(n):
                if a[i] > b[i]:
                    a[i], b[i] = b[i], a[i]
                    ops.append((3, i + 1))
                    changed = True
        print(len(ops))
        for op_type, idx in ops:
            print(f"{op_type} {idx}")

if __name__ == "__main__":
    solve()