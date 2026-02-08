import sys

data = sys.stdin.read().split()
if data:
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        s = data[idx]
        idx += 1
        n = len(s)
        
        first_right = -1
        for i in range(n):
            if s[i] == '>' or s[i] == '*':
                first_right = i
                break
      
        last_left = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '<' or s[i] == '*':
                last_left = i
                break
        
        if first_right != -1 and last_left != -1 and first_right < last_left:
            print("-1")
        else:
            max_time = 0
            for i in range(n):
                if s[i] == '<':
                    time = i + 1
                elif s[i] == '>':
                    time = n - i
                else:
                    time = max(i + 1, n - i)
                
                if time > max_time:
                    max_time = time
            print(max_time)