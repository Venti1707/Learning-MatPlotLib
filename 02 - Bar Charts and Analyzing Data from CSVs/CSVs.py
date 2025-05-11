# https://www.youtube.com/watch?v=nKxLfUrkLE8
import csv
from collections import Counter
from matplotlib import pyplot as plt

with open("02 - Bar Charts and Analyzing Data from CSVs/Data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

languages = []
users = []

for item in language_counter.most_common():
    languages.append(item[0])
    users.append(item[1])

languages.reverse()
users.reverse()

plt.barh(languages, users)
plt.xlabel("Users")
plt.title("Most popular programming languages")
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/02 - Bar Charts and Analyzing Data from CSVs/CSVs.png")
plt.show()