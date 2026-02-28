import sys
from collections import Counter

def solve():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    results = []

    for _ in range(t):
        n = int(input[idx])
        l_count = int(input[idx+1])
        r_count = int(input[idx+2])
        idx += 3
        
        socks = list(map(int, input[idx : idx + n]))
        idx += n
        
        left_socks = Counter(socks[:l_count])
        right_socks = Counter(socks[l_count:])
        
        for color in left_socks:
            if color in right_socks:
                match = min(left_socks[color], right_socks[color])
                left_socks[color] -= match
                right_socks[color] -= match
                l_count -= match
                r_count -= match
        
        if r_count > l_count:
            left_socks, right_socks = right_socks, left_socks
            l_count, r_count = r_count, l_count
            
        cost = 0
        diff = l_count - r_count 
        to_flip = diff // 2
        
        for color in left_socks:
            pairs_available = left_socks[color] // 2
            if pairs_available > 0 and to_flip > 0:
                take = min(pairs_available, to_flip)
                cost += take
                to_flip -= take
                l_count -= 2 * take 
        
        remaining_unmatched_pairs = (l_count + r_count) // 2
        results.append(cost + r_count + (to_flip * 2 if to_flip > 0 else 0))


def optimized_solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    t = int(next(it))
    
    for _ in range(t):
        n, l, r = int(next(it)), int(next(it)), int(next(it))
        colors = [int(next(it)) for _ in range(n)]
        
        L_map = Counter(colors[:l])
        R_map = Counter(colors[l:])
        
        for c in L_map:
            if c in R_map:
                m = min(L_map[c], R_map[c])
                L_map[c] -= m
                R_map[c] -= m
                l -= m
                r -= m
        
        if r > l:
            L_map, R_map = R_map, L_map
            l, r = r, l
            
        ans = 0
        diff = l - r
        for c in L_map:
            can_fix = L_map[c] // 2
            take = min(can_fix, diff // 2)
            ans += take
            diff -= 2 * take
            l -= 2 * take
            
        ans += diff + (l + r - diff) // 2
        print(ans)

if __name__ == "__main__":
    optimized_solve()