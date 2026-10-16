# SINIFLANDIRILMIŞ FREKANS SERİSİ

** Adım 1:** sınıf sayısı k'nın belirlenir
$$ k=1+3,322*\log_{10}n $$
# Burada k tamsayı olmalıdır. 
# Eğer k rasyonel bir sayı olarak elde edilirse bir üst tam sayıya yuvarlanır
* Adım 2:** sınıf genişliği c belirlenir
$$ c=\frac{x_{enb}-x_{enk}}{k} $$
** Adım 3** Sınıflar oluşturulur 
ilk sınıfın alt sınırı veri setindeki en küçük terim olarak alınır.
Bu sınıfa ait üst sınır ise $x_{enk}+c$ olarak belirlenir.
# ikinci sınıfın alt sınırı bir önceki sınıfın üst sınırı olmak üzere k sınıf benzer şekilde elde edilir
# ** ADım 4:** Sınıflara ait frekanslar belirlenir
# Bu adımda son sınıf hariç tüm sınıflarda
# $$x_{alt}leq x_i<x_{üst}$$
# koşulu geçerlidir. Son sınıfta ise 
# $$x_{alt}leq x_i\leq x_{üst}$$
# koşulu gözününde bulundurulur.