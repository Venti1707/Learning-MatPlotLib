# https://www.youtube.com/watch?v=XDv6T4a0RNc
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/06 - Histograms/Data.csv")
id = data["Responder_id"]
age = data["Age"]

bins = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]
median_age = 29

plt.hist(age, bins=bins, edgecolor="black", log=True)
plt.axvline(median_age, color="red", label="Median age")

plt.xlabel("Ages")
plt.ylabel("Total respondents")
plt.title("Age of respondents")
plt.legend()
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/06 - Histograms/Histograms.png")
plt.show()