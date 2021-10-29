import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('pima2.csv', usecols=['diabetes', 'age'])

group = {
    '20to30': pima[pima['age'] >= 20][pima['age'] < 31],
    '31to40': pima[pima['age'] >= 31][pima['age'] < 41],
    '41to50': pima[pima['age'] >= 41][pima['age'] < 51],
    '50plus': pima[pima['age'] >= 51]
}

for k, v in group.items():
    print(pd.crosstab(index=v['diabetes'], columns='count', colnames=[k]))
    print()
    plt.hist(v['diabetes'], **dict(alpha=0.5), label=k)

plt.legend()
plt.show()
