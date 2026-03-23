test = int(input())

for _ in range(test):
    strr = input()
    
    n = len(strr)
    res = [''] * 2 * n
    r = len(res) - 1
    l = 0
    
    for i in strr:
        res[r] = i
        res[l] = i
        r -= 1
        l += 1
    print(''.join(res))