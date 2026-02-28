import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t_cases = int(input_data[0])
    pointer = 1
    
    for _ in range(t_cases):
        s = input_data[pointer]
        t = input_data[pointer + 1]
        pointer += 2
        
        v = [0] * 26
        for char in t:
            v[ord(char) - ord('a')] += 1
            
        possible = True
        for char in s:
            idx = ord(char) - ord('a')
            v[idx] -= 1
            if v[idx] < 0:
                possible = False
                break
        
        if not possible:
            print("Impossible")
            continue
            
        res = []
        for char in s:
            char_idx = ord(char) - ord('a')
            for u in range(char_idx):
                if v[u] > 0:
                    res.append(chr(ord('a') + u) * v[u])
                    v[u] = 0
            res.append(char)
        for u in range(26):
            if v[u] > 0:
                res.append(chr(ord('a') + u) * v[u])
        
        print("".join(res))

if __name__ == "__main__":
    solve()