test = int(input())

for _ in range(test):
    w = input()
    p = int(input())
    
    summ = 0
    counts = [0] * 27 
    for char in w:
        val = ord(char) - ord('a') + 1
        summ += val
        counts[val] += 1
   
    # Fix: Added descending loop and moved it outside character counting
    for i in range(26, 0, -1):
        while counts[i] > 0 and summ > p:
            summ -= i
            counts[i] -= 1
          
    res = []
    for char in w:
        val = ord(char) - ord('a') + 1
        if counts[val] > 0:
            res.append(char)
            counts[val] -= 1 
            
    print(''.join(res))