x = [18, 32, 65, 58, 87, 74, 69, 52, 80, 70, 42, 58]

n = len(x)

for i in range(n-1):
    for j in range(i+1, n):
        if x[i] > x[j]:
            gec = x[i]
            x[i] = x[j]
            x[j] = gec

print("Sıralı x: ", x)
