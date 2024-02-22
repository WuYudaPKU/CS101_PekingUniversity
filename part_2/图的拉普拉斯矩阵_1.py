n, m = map(int, input().split())

matrix_a = [[0] * n for _ in range(n)]
matrix_d = [[0] * n for _ in range(n)]
matrix_l = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix_a[a][b] = 1
    matrix_a[b][a] = 1
    matrix_d[a][a] += 1
    matrix_d[b][b] += 1

for row in range(n):
    for column in range(n):
        matrix_l[row][column] = matrix_d[row][column] - matrix_a[row][column]

for row in matrix_l:
    temp = [str(m) for m in row]
    print(" ".join(temp))
