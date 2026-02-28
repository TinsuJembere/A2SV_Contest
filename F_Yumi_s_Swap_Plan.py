import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        s = sys.stdin.readline().strip()
    except EOFError:
        return

    total_h = s.count('H')
    
    if total_h == 0 or total_h == n:
        print(0)
        return

    extended_s = s + s
    
    current_t_count = extended_s[:total_h].count('T')
    min_swaps = current_t_count
    
    for i in range(1, n):
        if extended_s[i-1] == 'T':
            current_t_count -= 1
        if extended_s[i + total_h - 1] == 'T':
            current_t_count += 1
            
        if current_t_count < min_swaps:
            min_swaps = current_t_count
            
    print(min_swaps)

if __name__ == '__main__':
    solve()