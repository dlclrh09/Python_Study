import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('pima2.csv', usecols=['diabetes', 'pregnant'])

group = {
    '0to5': pima[pima['pregnant'] >= 0][pima['pregnant'] < 6],
    '6to10': pima[pima['pregnant'] >= 6][pima['pregnant'] < 11],
    '10plus': pima[pima['pregnant'] >= 11]
}

for k, v in group.items():
    print(pd.crosstab(index=v['diabetes'], columns='count', colnames=[k]))
    print()
    plt.hist(v['diabetes'], **dict(alpha=0.5), label=k)

plt.legend()
plt.show()