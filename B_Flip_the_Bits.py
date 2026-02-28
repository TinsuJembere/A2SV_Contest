import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        a = next(it)
        b = next(it)
        
        valid_points = []
        count0 = 0
        count1 = 0
        for i in range(n):
            if a[i] == '0':
                count0 += 1
            else:
                count1 += 1
            if count0 == count1:
                valid_points.append(i)
        
        possible = True
        last_point = -1
        
        for point in valid_points:
            segment_a = a[last_point + 1 : point + 1]
            segment_b = b[last_point + 1 : point + 1]
            
            if segment_a != segment_b:
                is_inverted = all(segment_a[j] != segment_b[j] for j in range(len(segment_a)))
                if not is_inverted:
                    possible = False
                    break
            last_point = point
            
        if last_point < n - 1:
            if a[last_point + 1:] != b[last_point + 1:]:
                possible = False
        
        print("YES" if possible else "NO")

if __name__ == "__main__":
    solve()