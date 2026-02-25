import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    a = list(map(int, input_data[2:2+n]))
    b = list(map(int, input_data[2+n:]))
    
    res = []
    i = 0  
    j = 0 
    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res.extend(a[i:])
    res.extend(b[j:])
    print(*(res))

if __name__ == "__main__":
    solve()