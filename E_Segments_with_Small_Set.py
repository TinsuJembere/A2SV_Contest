import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:]))
    
    freq = [0] * 100001
    distinct_count = 0
    l = 0
    total_good_segments = 0
    
    for r in range(n):
        val_r = a[r]
        if freq[val_r] == 0:
            distinct_count += 1
        freq[val_r] += 1
        
        while distinct_count > k:
            val_l = a[l]
            freq[val_l] -= 1
            if freq[val_l] == 0:
                distinct_count -= 1
            l += 1
        
        total_good_segments += (r - l + 1)
        
    print(total_good_segments)

if __name__ == "__main__":
    solve()