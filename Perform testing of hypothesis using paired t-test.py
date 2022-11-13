import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Blood_Pressure.csv")
print(df[['bp_before', 'bp_after']].describe())
plt.savefig('boxplot_outliers.png')
df['bp_difference'] = df['dp_before'] - df['bp_after']
df['bp_difference'].plot(kind = 'hist', title = 'Blood Pressure Difference Histogram')
plt.savefig('blood pressure difference histogram.png')
stats.probplot(df['bp_difference'], plot = plt)
plt.title('blood pressure difference qq plot.png')
stats.sharipo(df['bp_difference'])
stats.ttest_rel(df['dp_before'], df['bp_after'])