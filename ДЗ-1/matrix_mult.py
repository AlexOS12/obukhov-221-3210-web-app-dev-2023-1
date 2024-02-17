def mat_mult(a, b):
    n = len(a)
    mtx = [[0] * n for i in range(n)]

    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mtx[i][j] += a[i][k] * b[k][j]                       

    return mtx
        
n = int(input())
a, b = [], []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

for line in mat_mult(a, b):
    print(*line)
