# sınıflandırılmış frekans serisi oluşturma
import math
veri = [15, 23, 23, 46, 38, 32, 54, 45, 65, 49, 57,
        81, 72, 66, 54, 10, 75, 58, 47, 66, 59, 74, 87]
x = sorted(veri)
n = len(x)
xenk = min(x)
xenb = max(x)
print("Gözlem sayısı n:", n)
print("Xenk=", xenk)
print("Xenb=", xenb)

# math.ceil() bir üst tamsayıya yuvarlar
# math.log10() 10 tabanında logaritma değerini verir.

# sınıf sayısı k tam sayı olarak belirlendi
k = math.ceil(1+3.322*math.log10(n))
c = (xenb-xenk)/k  # sınıf aralığı c belirlendi
print("Sınıf sayısı k=", k)
print("Sınıf aralığı c=", round(c, 2))
alt_sınır = [xenk]
üst_sınır = [xenk+c]
orta_nokta = [(alt_sınır[0]+üst_sınır[0])/2]
for i in range(1, k):
    alt_sınır.append(üst_sınır[i-1])
    üst_sınır.append(alt_sınır[i]+c)
    orta_nokta.append((alt_sınır[i]+üst_sınır[i])/2)

frekanslar = []
for i in range(k):
    sayac = 0
    for deger in x:
        if i == k-1:
            if alt_sınır[i] <= deger <= üst_sınır[i]:
                sayac += 1
        else:
            if alt_sınır[i] <= deger < üst_sınır[i]:
                sayac += 1
    frekanslar.append(sayac)
b_frekanslar = [frekanslar[0]]
for i in range(1, k):
    b_frekanslar.append(b_frekanslar[i-1]+frekanslar[i])


toplam = 0
for i in range(k):
    toplam += orta_nokta[i]*frekanslar[i]
ortalama = toplam/n

toplam2 = 0
for i in range(k):
    toplam2 += ((orta_nokta[i]-ortalama)**2)*frekanslar[i]
varyans = toplam2/(n-1)

for i in range(k):
    if b_frekanslar[i] > (n/2):
        medyan_sınıfı = i
        break
medyan = alt_sınır[medyan_sınıfı] + \
    (n/2-b_frekanslar[medyan_sınıfı-1])*(c/frekanslar[medyan_sınıfı])

for i in range(k):
    if frekanslar[i] == max(frekanslar):
        mod_sınıfı = i
        break
delta1 = frekanslar[mod_sınıfı]-frekanslar[mod_sınıfı-1]
delta2 = frekanslar[mod_sınıfı]-frekanslar[mod_sınıfı+1]
mod_değ = alt_sınır[mod_sınıfı]+(delta1/(delta1+delta2))*c

print(f"{'-'*70}")
print(f"{'Sınıflar':^20}{'Orta Nokta':^20}{'Frekanslar':^20}{'B.Frekanslar':^10}")
print(f"{'-'*70}")
for i in range(k):
    print(
        f"{round(alt_sınır[i], 2):^10}-{round(üst_sınır[i], 2):^10}{round(orta_nokta[i], 2):^20}{frekanslar[i]:^20}{b_frekanslar[i]:^10}")
print(f"{'-'*70}")

print("Ortalama=", round(ortalama, 2))
print("Varyans=", round(varyans, 2))
print("Standart sapma=", round(varyans**0.5, 2))
print("Standart hata=", round((varyans/n)**0.5, 2))
print("Medyan sınıfı=", medyan_sınıfı+1)
print("Medyan=", round(medyan, 2))
print("Mod sınıfı=", mod_sınıfı+1)
print("Mod=", round(mod_değ, 2))
