import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = input_data[2:]
    
    # Frequency map to track unique elements in the window
    counts = {}
    distinct_count = 0
    left = 0
    max_len = -1
    ans_l, ans_r = 0, 0
    
    for right in range(n):
        val_r = a[right]
        
        # Add right element to window
        if val_r not in counts or counts[val_r] == 0:
            distinct_count += 1
            counts[val_r] = 1
        else:
            counts[val_r] += 1
            
        # If too many unique elements, shrink from the left
        while distinct_count > k:
            val_l = a[left]
            counts[val_l] -= 1
            if counts[val_l] == 0:
                distinct_count -= 1
            left += 1
            
        # Check if this is the longest segment found so far
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            ans_l, ans_r = left + 1, right + 1
            
    # Print 1-based indices
    print(f"{ans_l} {ans_r}")

if __name__ == "__main__":
    solve()