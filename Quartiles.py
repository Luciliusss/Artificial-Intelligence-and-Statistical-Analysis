import random

x = [27, 29, 31, 33, 35, 36, 36, 39, 41, 43, 52, 89]

n = len(x)
if n % 4 == 0:
    Q1 = (x[n//4 - 1] + x[n//4]) / 2
else:
    Q1 = x[n//4]

if n % 2 == 0:
    Q2 = (x[n//2 - 1] + x[n//2]) / 2
else:
    Q2 = x[n//2]

if n % 4 == 0:
    Q3 = (x[3*n//4 - 1] + x[3*n//4]) / 2
else:
    Q3 = x[3*n//4]

IQR = Q3 - Q1
alt = Q1 - 1.5*IQR
ust = Q3 + 1.5*IQR

aykiri = []
for i in range(n):
    if x[i] < alt or x[i] > ust:
        aykiri.append(x[i])
print("aykırı değerler:", aykiri)
