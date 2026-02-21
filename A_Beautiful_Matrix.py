row_of_one = 0
col_of_one = 0

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            row_of_one = i + 1
            col_of_one = j + 1
moves = abs(3 - row_of_one) + abs(3 - col_of_one)
print(moves)