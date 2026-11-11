veri = [23, 10, 42, 28, 33, 19, 27, 35, 48, 52, 21, 18, 30, 45, 39, 26, 31, 41, 22, 29,
        34, 37, 40, 16, 25, 44, 49, 50, 20, 32, 38, 43, 24, 27, 36, 47, 51, 17, 31, 86]

x = sorted(veri)

n = len(x)

if n % 4 == 0:
    Q1 = (1/2)*((x[n//4-1])+(x[n//4]))
    Q3 = (1/2)*((x[3*n//4-1])+(x[3*n//4]))
else:
    Q1 = (x[n//4])
    Q3 = (x[3*n//4])

if n % 2 == 0:
    Q2 = (1/2)*(x[n//2-1]+x[n//2])
else:
    Q2 = x[n//2]

IQR = Q3 - Q1


if x[0] > Q1 - 1.5*IQR:
    alt = x[0]
else:
    alt = Q1 - 1.5*IQR

if x[n-1] < Q3 + 1.5*IQR:
    üst = x[n-1]
else:
    üst = Q3 + 1.5*IQR


aykırı_eleman = []

for eleman in x:
    if eleman < alt or eleman > üst:
        aykırı_eleman.append(eleman)

print("X = ", x)
print("n = ", n)
print("Q1 = ", Q1)
print("Q2 = ", Q2)
print("Q3 = ", Q3)
print("IQR = ", IQR)
print("Alt sınır : ", alt)
print("Üst sınır : ", üst)
