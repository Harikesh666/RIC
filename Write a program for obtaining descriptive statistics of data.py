import pandas as pd

d = {'Age' : pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]), 'Rating' : pd.Series([4.23, 3.34, 3.98, 2.56, 3.20, 4.60, 3.80, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(d)

print(df)

print("------SUM------")
print(df.sum())

print("------MEAN------")
print(df.mean())

print("------STANDARD DEVIATION------")
print(df.std())

print("------DEESCRIPTIVE STATISTICS-------")
print(df.describe())