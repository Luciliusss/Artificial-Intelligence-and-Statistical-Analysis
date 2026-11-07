from scipy import stats

x = [38, 42, 58, 64, 53, 29, 72, 56, 80, 62]

mu0 = 40
alfa = 0.05
alternatif = "küçük"
n = len(x)
T = sum(x)
Xort = T/n
toplam = 0

for i in range(n):
    toplam += (x[i]-Xort)**2

gkt = toplam

s2 = gkt/(n-1)

s = s2**0.5

shata = s/(n**0.5)

thesap = (Xort - mu0)/shata  # t değeri hesaplandı.

if alternatif == 'farklı':
    t_tablo = stats.t.ppf(1-alfa/2, n-1)
    if abs(thesap) > t_tablo:
        karar = "H0 red"
    else:
        karar = "H0 red edilemez"
elif alternatif == "büyük":
    t_tablo = stats.t.ppf(1-alfa, n-1)
    if thesap > t_tablo:
        karar = "H0 red"
    else:
        karar = "H0 red edilemez"
elif alternatif == "küçük":
    t_tablo = stats.t.ppf(alfa, n-1)
    if thesap < t_tablo:
        karar = "H0 red"
    else:
        karar = "H0 red edilemez"

print("xort= ", round(Xort, 3))
print("Örneklem Varyansı = ", round(s2, 2))
print("thesap = ", round(thesap, 3))
print("Serbestlik derecesi", n-1)
print("ttablo = ", round(t_tablo, 3))
print("Karar: ", karar)
