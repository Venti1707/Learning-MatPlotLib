# https://www.youtube.com/watch?v=nKxLfUrkLE8
import numpy as np
from matplotlib import pyplot as plt

ages_x = [18, 19, 20, 21, 22]
x_indexes = np.arange(len(ages_x))
width = 0.25

py_dev_y = [20046, 17100, 20000, 24744, 30500]
plt.bar(x_indexes - width, py_dev_y, width=width, label="Python", linewidth=2, color="#008FD5")

js_dev_y = [16446, 16791, 18942, 21780, 25704]
plt.bar(x_indexes, js_dev_y, width=width, label="JavaScript", linewidth=2, color="#E5AE38")

all_dev_y = [17784, 16500, 18012, 20628, 25206]
plt.bar(x_indexes + width, all_dev_y, width=width, label="All", color="#444444")

plt.title("Median salary (USD) by age")
plt.xlabel("Age")
plt.ylabel("Median salary (USD)")
plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/02 - Bar Charts and Analyzing Data from CSVs/Bar Charts.png")
plt.show()