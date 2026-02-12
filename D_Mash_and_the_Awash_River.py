t = int(input())
for _ in range(t):
    s = input()
    if '**' in s or '*<' in s or '>*' in s or '><' in s:
        print(-1)
 
    else:
       max_ = 0
       for i in range(len(s)):
           if s[i] == '<':
               max_ = max(max_, i + 1)
        
           elif s[i] == '>':
               max_ = max(max_, len(s) - i)
        
           else:
            max_ = max(max_, i + 1, len(s) - i)
    
       print(max_)