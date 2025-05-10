# https://www.youtube.com/watch?v=xN-Supd4H38

from matplotlib import pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
labels=["Developer 1", "Developer 2", "Developer 3"]
colors=["#6D904F", "#FC4F30", "#008FD5"]

plt.stackplot(hours, [dev1, dev2, dev3], labels=labels, colors=colors)

plt.title("Hours coded over time")
plt.legend()
plt.style.use('fivethirtyeight')
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/04 - Stack Plots/Stack Plots.png")
plt.show()