import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('pima2.csv', usecols=['diabetes', 'age'])
pima["grade"] = ""
print(pima['grade'][0])
for i in range(len(pima['age'])):
    grade = '50plus'
    if 20 <= pima['age'][i] <= 30:
        grade = '20to30'
    elif 31 <= pima['age'][i] <= 40:
        grade = '31to40'
    elif 41 <= pima['age'][i] <= 50:
        grade = '41to50'
    pima['grade'][i] = grade
# print(pima['grade'])
table = pd.crosstab(index=pima['grade'], columns=pima['diabetes'])
print(table)

table.plot.bar(stacked=True)
plt.legend()
plt.show()

# group = {
#     '20to30': pima[pima['age'] >= 20][pima['age'] < 31],
#     '31to40': pima[pima['age'] >= 31][pima['age'] < 41],
#     '41to50': pima[pima['age'] >= 41][pima['age'] < 51],
#     '50plus': pima[pima['age'] >= 51]
# }
#
# for k, v in group.items():
#     print(pd.crosstab(index=v['diabetes'], columns='count', colnames=[k]))
#     print()
#     plt.hist(v['diabetes'], **dict(alpha=0.5), label=k)
#
#
# plt.legend()
# plt.show()
