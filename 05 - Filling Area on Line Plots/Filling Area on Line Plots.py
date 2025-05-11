# https://www.youtube.com/watch?v=x0Uguu7gqgk

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/05 - Filling Area on Line Plots/Data.csv")
ages = data["Age"]
allSalaries = data["All_Devs"]
pySalaries = data["Python"]

plt.plot(ages, allSalaries, label="All", linewidth=2)
plt.plot(ages, pySalaries, label="Python", linewidth=2)
plt.fill_between(ages, pySalaries, allSalaries, alpha=0.25, where=(pySalaries > allSalaries), color="green", interpolate=True, label="Above average")
plt.fill_between(ages, pySalaries, allSalaries, alpha=0.25, where=(pySalaries <= allSalaries), color="red", interpolate=True, label="Below average")

plt.title("Median salary (USD) by age")
plt.xlabel("Age")
plt.ylabel("Median salary (USD)")
plt.legend()
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/05 - Filling Area on Line Plots/Filling Area on Line Plots.png")
plt.show()