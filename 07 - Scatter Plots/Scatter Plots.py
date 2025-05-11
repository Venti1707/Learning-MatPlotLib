# https://www.youtube.com/watch?v=zZZ_RCwp49g
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/07 - Scatter Plots/Data.csv")

view_count = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(view_count, likes, c=ratio, cmap="summer", edgecolors="black", linewidth=1, alpha=0.75)
cbar = plt.colorbar()
cbar.set_label("Like to dislike ratio")
plt.xscale("log")
plt.yscale("log")

plt.title("Trending YouTube videos")
plt.xlabel("View count")
plt.ylabel("Total likes")
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/07 - Scatter Plots/Scatter Plots.png")
plt.show()