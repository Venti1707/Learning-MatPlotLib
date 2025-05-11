# https://www.youtube.com/watch?v=_LWjaAiKaf8
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd

data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/10 - Subplots/Data.csv")
ages = data["Age"]
allSalaries = data["All_Devs"]
pySalaries = data["Python"]
jsSalaries = data["JavaScript"]

plot1, ax1 = plt.subplots()
plot2, ax2 = plt.subplots()

ax1.plot(ages, allSalaries, label="All developers")
ax1.legend()
ax2.set_xlabel("Ages")
ax1.set_ylabel("Median Salary (USD)")

ax2.plot(ages, pySalaries, label="Python developers")
ax2.plot(ages, jsSalaries, label="JavaScript developers")
ax2.legend()
ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary (USD)")

plot1.tight_layout()
plot2.tight_layout()
plt.show()

plot1.savefig("C:/OtherProjects/Learning-MatPlotLib/10 - Subplots/Plot 1.png")
plot2.savefig("C:/OtherProjects/Learning-MatPlotLib/10 - Subplots/Plot 2.png")