"""
beautiful_kuku.py を実装してください
式が表示されている
結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
※結果が3桁の場合は崩れてもOKです

"""
rows = int(input("行数を入力してください:"))
columns = int(input("列数を入力してください:"))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(f'{i} x {j} = {i * j:2d}', end=' | ')
    print()
