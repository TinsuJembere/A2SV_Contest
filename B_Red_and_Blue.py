import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        r = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        m = int(input_data[idx])
        idx += 1
        b = [int(x) for x in input_data[idx:idx+m]]
        idx += m
        
        max_r = 0
        curr_sum = 0
        for x in r:
            curr_sum += x
            if curr_sum > max_r:
                max_r = curr_sum
                
        max_b = 0
        curr_sum = 0
        for x in b:
            curr_sum += x
            if curr_sum > max_b:
                max_b = curr_sum
        
        results.append(str(max_r + max_b))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()