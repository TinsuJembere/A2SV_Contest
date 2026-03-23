import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        p = list(map(int, input[ptr : ptr + n]))
        ptr += n
        
        ans = []
        for i in range(n):
            if i == 0 or i == n - 1:
                ans.append(p[i])
            else:
                if not (p[i-1] < p[i] < p[i+1]) and not (p[i-1] > p[i] > p[i+1]):
                    ans.append(p[i])
        
        results.append(f"{len(ans)}")
        results.append(" ".join(map(str, ans)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()