from scipy import stats
import numpy as np

Vize = np.array[52, 84, 42, 58, 64, 72, 66, 52]
Final = np.array[68, 86, 40, 72, 70, 70, 82, 64]

n = len(Vize)

d = Vize - Final
print("Farklar: ", d)

dort = np.mean(d)
print("Ortalama Fark", dort)

s_d = np.std(d, ddof=1)
print("Standart sapma", s_d)
