import pandas as pd
import matplotlib.pyplot as plt

diabetes = pd.read_csv('pima2.csv')

countTable = pd.crosstab(columns='count', index=diabetes['diabetes'])
rateTable = pd.crosstab(columns='count', index=diabetes['diabetes'], normalize='columns')

countTable.plot.bar()
rateTable.plot.pie(subplots=True)
plt.show()