import pandas as pd

df = pd.DataFrame({"Gozlem_No": range(1, 9),
                   "Vize": [52, 84, 42, 58, 64, 72, 66, 52],
                   "Final": [68, 86, 40, 72, 70, 70, 82, 64]})

df["Fark"] = df["Vize"] - df["Final"]
print(df)
