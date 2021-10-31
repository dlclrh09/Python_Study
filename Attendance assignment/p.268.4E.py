import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('pima2.csv', usecols=['diabetes', 'pregnant'])
pima["grade"] = ""
print(pima['grade'][0])
for i in range(len(pima['pregnant'])):
    grade = '10plus'
    if 0 <= pima['pregnant'][i] <= 5:
        grade = '0to5'
    elif 6 <= pima['pregnant'][i] <= 10:
        grade = '6to10'
    pima['grade'][i] = grade
# print(pima['grade'])
table = pd.crosstab(index=pima['grade'], columns=pima['diabetes'])
print(table)

table.plot.bar(stacked=True)
plt.legend()
plt.show()