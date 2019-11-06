rows = int(input("行数を入力してください:"))
columns = int(input("列数を入力してください:"))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(f'{i} x {j} = {i * j:2d}', end=' | ')
    print()
