import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0]) 
    ptr = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr+1])
        s = input_data[ptr+2]
        ptr += 3
        
        current_w_count = 0
        for i in range(k):
            if s[i] == 'W':
                current_w_count += 1
        
        min_recolor = current_w_count
        
        for i in range(k, n):
            if s[i] == 'W':
                current_w_count += 1
            if s[i - k] == 'W':
                current_w_count -= 1
            
            if current_w_count < min_recolor:
                min_recolor = current_w_count
                
            if min_recolor == 0:
                break
        
        results.append(str(min_recolor))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()