import sys

def solve():
    n, x, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    time_to_first_zero = -1
    current_pos = x
    
    for i in range(min(n, k)):
        if s[i] == 'L':
            current_pos -= 1
        else:
            current_pos += 1
        
        if current_pos == 0:
            time_to_first_zero = i + 1
            break

    if time_to_first_zero == -1:
        print(0)
        return

    ans = 1
    remaining_k = k - time_to_first_zero

    time_to_cycle_zero = -1
    current_pos = 0
    for i in range(n):
        if s[i] == 'L':
            current_pos -= 1
        else:
            current_pos += 1
        
        if current_pos == 0:
            time_to_cycle_zero = i + 1
            break

    if time_to_cycle_zero != -1:
        ans += (remaining_k // time_to_cycle_zero)

    print(ans)

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()