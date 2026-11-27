from scipy import stats

Vize = [52, 84, 42, 58, 64, 72, 66, 52]
Final = [68, 86, 40, 72, 70, 70, 82, 64]

n = len(Vize)
d = []

for i in range(n):
    d.append(Vize[i]-Final[i])

print("Farklar: ", d)

dort = sum(d)/n
print("Ortalama Fark", dort)

toplam = 0

for i in range(n):
    toplam += (d[i]-dort)**2

s_d = (toplam / (n-1))**0.5
print("Standart Sapma(d): ", round(s_d, 4))

s_hata = s_d / (n**0.5)
print("Standard hata: ", round(s_hata, 4))

thesap = dort / s_hata
print("thesap: ", round(thesap, 4))

ttablo = stats.t.ppf(0.05, n-1)
print("ttablo: ", round(ttablo, 4))

if abs(thesap) > abs(ttablo):
    karar = 'H0 reddedilir'
else:
    karar = 'reddedilemez'

print(karar)
