# Frekans serisi oluşturma kod yazımı
x = [8, 8, 9, 7, 7, 7, 6, 6, 5, 5, 9, 4, 3, 3, 2, 1, 6,
     4, 3, 7, 8, 4, 10, 6, 8, 7, 1, 3, 4, 2, 8, 9, 10, 7]
n = len(x)  # len(x) x listesindeki gözlem sayısını verir
x = sorted(x)  # sorted(x) x listesindeki gözlemleri küçükten büyüğe sıralar
xi = [x[0]]
frekans = [1]
r = 0
for değer in x:
    if xi[r] == değer:
        frekans[r] += 1
    else:
        # append() fonksiyonu parantez içindeki ifadeyi listeye eklemek için kullanılır.
        xi.append(değer)
        # frekans.apend(1) frekans listesine 1 değerini ekler.
        frekans.append(1)
        r += 1

# print(f"") ifadesi, metinleri ve değişken değerlerini biçimlendirmek için kullanılır.
# f"" formatında, değişkenler ve ifadeler {} süslü parantezleri içinde yazılır.
# Süslü parantezler içinde doğrudan metin yazılacaksa metin, tek tırnak kullanılarak yazılır.
# Örneğin: {'x(i)':<10}
# {'x(i)':<10} kullanımı, x(i) metnini 10 karakterlik bir alana sola hizalı yazar.
# {'Frekans':>10} kullanımı, Frekans metnini 10 karakterlik bir alana sağa hizalı yazar.
# {'Frekans':^10} kullanımı, Frekans metnini 10 karakterlik bir alana ortalı yazar.
# {xi[i]:<10} kullanımı, xi[i] değişkeninin değerini 10 karakterlik bir alana sola hizalı yazar.
# Değişken adı tırnak içine alınmaz.
# print("-"*24) ifadesi, "-" karakterini art arda 24 kez yazar.

print(f"{'x(i)':<10} {'Frekans':>10}")
print("-"*24)
k = len(xi)
for i in range(k):
    print(f"{xi[i]:<10} {frekans[i]:>10}")
print("-"*24)
