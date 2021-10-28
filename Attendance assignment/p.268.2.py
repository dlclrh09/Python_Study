import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns = ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age']
pima = pd.read_csv('pima2.csv', usecols=['diabetes'] + columns)

table = pima.groupby('diabetes')

print("최솟값")
print(table.min())
print("최댓값")
print(table.max())
print("중앙값")
print(table.median())
print("평균")
print(table.mean())
print("제 1사분위수")
print(table.quantile(.25))
print("제 3사분위수")
print(table.quantile(.75))

for name, data in table:
    for column in columns:
        plt.hist(data[column], label=name + " " + column)
        plt.legend()
        plt.show()

sns.set(style="whitegrid")
for name, data in table:
    sns.boxplot(data=data).set_title(name)
    plt.show()