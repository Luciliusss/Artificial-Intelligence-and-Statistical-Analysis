x = [8, 8, 9, 7, 7, 7, 6, 6, 5, 5, 9, 4, 3, 3, 2, 1, 6,
     4, 3, 7, 8, 4, 10, 6, 7, 7, 1, 3, 4, 2, 8, 9, 10, 8]
n = len(x)
x = sorted(x)

y = []
frekans = [1]

y.append(x[0])

r = 0
for i in range(1, n):
    if y[r] == x[i]:
        frekans[r] += 1
    else:
        y.append(x[i])
        frekans.append(1)
        r += 1
print(y)
print(frekans)
print(f"{'x(i)':^10} {'frekans':^12}")
print("-" * 24)

k = len(y)
for i in range(k):
    print(f"{y[i]:^10} {frekans[i]:^12}")
print("-" * 24)
