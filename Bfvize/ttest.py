from scipy import stats

x = [38, 42, 58, 64, 53, 29, 72, 56, 80, 62]

mu0 = 50
afla = 0.05

n = len(x)
T = sum(x)

xort = T/n

toplam = 0
for i in range(n):
    toplam += (x[i] - xort)**2
ornek_varyans = toplam/(n-1)
standart_sapma = ornek_varyans**0.5
shata = standart_sapma/(n**0.5)
thesap = (xort - mu0)/shata

if alternatif == "farkli":
    t_tablo = stats.t.ppf(1 - alfa/2, n-1)
if alternatif == "buyuk":
    t_tablo = stats.t.ppf(1 - alfa, n-1)
if alternatif == "kucuk":
    t_tablo = stats.t.ppf(alfa, n-1)

print("xort:", xort)
print("ornek_varyans:", ornek_varyans)
print("standart_sapma:", standart_sapma)
print("ttablo:", t_tablo)

if alternatif == "farkli" and abs(thesap) > t_tablo:
    print("H0 reddedilir")
else:
    print("H0 reddedilemez")

if alternatif == "buyuk" and thesap > t_tablo:
    print("H0 reddedilir")
else:
    print("H0 reddedilemez")

if alternatif == "kucuk" and thesap < t_tablo:
    print("H0 reddedilir")
else:
    print("H0 reddedilemez")
