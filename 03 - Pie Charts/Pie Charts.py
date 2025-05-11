# https://www.youtube.com/watch?v=MPiz50TsyF0
from matplotlib import pyplot as plt

languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
users = [59219, 55466, 47544, 36443, 35917]
explode = [0, 0, 0, 0.1, 0]

plt.pie(users, labels=languages, explode=explode, wedgeprops={"edgecolor": "black"}, shadow=True, startangle=90, autopct='%1.1f%%')

plt.title("Top 5 most used programming languages")
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/03 - Pie Charts/Pie Charts.png")
plt.show()