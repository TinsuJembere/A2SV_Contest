import sys
input = sys.stdin.read

def solve():
    data = input().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        b = list(map(int, data[idx:idx+n])); idx += n
        
        ops = []
        
        # Position maps
        posA = {}
        posB = {}
        for i in range(n):
            posA[a[i]] = i
            posB[b[i]] = i
        
        # Helper swaps
        def swap_a(i):
            a[i], a[i+1] = a[i+1], a[i]
            posA[a[i]] = i
            posA[a[i+1]] = i+1
            ops.append((1, i+1))
        
        def swap_b(i):
            b[i], b[i+1] = b[i+1], b[i]
            posB[b[i]] = i
            posB[b[i+1]] = i+1
            ops.append((2, i+1))
        
        def swap_ab(i):
            a[i], b[i] = b[i], a[i]
            posA[a[i]] = i
            posB[b[i]] = i
            ops.append((3, i+1))
        
        # Place values 1..n into array a
        for v in range(1, n+1):
            target = v - 1
            
            if v in posA:
                i = posA[v]
                # bubble left in a
                while i > target:
                    swap_a(i-1)
                    i -= 1
            else:
                i = posB[v]
                # bubble left in b
                while i > target:
                    swap_b(i-1)
                    i -= 1
                # now at correct index, swap arrays
                swap_ab(target)
        
        # Now place values n+1..2n into array b
        for v in range(n+1, 2*n+1):
            target = v - n - 1
            
            if v in posB:
                i = posB[v]
                while i > target:
                    swap_b(i-1)
                    i -= 1
            else:
                i = posA[v]
                while i > target:
                    swap_a(i-1)
                    i -= 1
                swap_ab(target)
        
        # Output
        out.append(str(len(ops)))
        for tpe, i in ops:
            out.append(f"{tpe} {i}")
    
    print("\n".join(out))

if __name__ == "__main__":
    solve()