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
        k = int(input[ptr+1])
        ptr += 2
        a = []
        for i in range(n):
            a.append(int(input[ptr + i]))
        ptr += n
        a.sort()
        
        unique_vals = []
        val_counts = []
        
        if n > 0:
            current_val = a[0]
            current_cnt = 0
            for x in a:
                if x == current_val:
                    current_cnt += 1
                else:
                    unique_vals.append(current_val)
                    val_counts.append(current_cnt)
                    current_val = x
                    current_cnt = 1
            unique_vals.append(current_val)
            val_counts.append(current_cnt)
        
        m = len(unique_vals)
        max_cards = 0
        current_window_sum = 0
        left = 0
        
        for right in range(m):
            current_window_sum += val_counts[right]
            
            if right > 0 and unique_vals[right] != unique_vals[right-1] + 1:
                left = right
                current_window_sum = val_counts[right]
            
            while (right - left + 1) > k:
                current_window_sum -= val_counts[left]
                left += 1
            
            if current_window_sum > max_cards:
                max_cards = current_window_sum
        
        results.append(str(max_cards))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()