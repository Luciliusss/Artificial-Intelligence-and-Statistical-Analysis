import math

veri = [15, 23, 11, 46, 38, 32, 54, 45, 65, 49, 72, 66, 54,
        10, 75, 58, 47, 66, 66, 59, 74, 81]

x = sorted(veri)
n = len(x)
xenk = min(x)
xenb = max(x)

print("Veri seti:", x)

print("Xenk=", xenk)
print("Xenb=", xenb)

# math.ceil() fonksiyonu ile k sayısı yukarı
k = math.ceil(1 + 3.322 * math.log10(n))
c = (xenb - xenk) / k

print("Sınıf sayısı k =", k)
print("Sınıf genişliği c =", c)

alt_sınır = [xenk]
üst_sınır = [xenk + c]

for i in range(1, k):
    alt_sınır.append(üst_sınır[i - 1])
    üst_sınır.append(alt_sınır[i] + c)

print("Alt Sınırlar:", [round(val, 2) for val in alt_sınır])
print("Üst Sınırlar:", [round(val, 2) for val in üst_sınır])

frekanslar = []
sayac = 0
for i in range(k):
    sayac = 0
    for j in x:
        if i == k-1:
            if alt_sınır[i] <= j <= üst_sınır[i]:
                sayac += 1
        else:
            if alt_sınır[i] <= j < üst_sınır[i]:
                sayac += 1
    frekanslar.append(sayac)

print(f"{'sınıflar':<10}{'frekanslar'}")
print("-" * 24)

for i in range(k):
    print(
        f"{round(alt_sınır[i], 2)} - {round(üst_sınır[i], 2)}-----{frekanslar[i]}")
