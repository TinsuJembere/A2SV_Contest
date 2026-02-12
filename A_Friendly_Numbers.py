def sum_of_digits(n):
    return sum(int(c) for c in str(n))

def friendly_numbers(x):
    count = 0
    for d in range(1, 100):  
        y = x + d
        if sum_of_digits(y) == d:
            count += 1
    return count

t = int(input())
for _ in range(t):
    x = int(input())
    print(friendly_numbers(x))
