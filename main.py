import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

censusFilePath = "../datasets/census2018.csv"
sb.set(style = 'darkgrid')
census = pd.read_csv(censusFilePath)
print(census)
plt.show()
