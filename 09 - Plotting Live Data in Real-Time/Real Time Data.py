# https://www.youtube.com/watch?v=Ercd-Ip5PfQ
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from itertools import count
from matplotlib.animation import FuncAnimation
import pandas as pd
import random

x_vals = []
y_vals = []
index = count()

def animate(i):
    data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/09 - Plotting Live Data in Real-Time/Data.csv")
    x = data["x_value"]
    y1 = data["total_1"]
    y2 = data["total_2"]
    plt.cla()
    plt.plot(x, y1, label="Channel 1")
    plt.plot(x, y2, label="Channel 2")
    plt.legend(loc="upper left")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.xlabel("Time")
plt.ylabel("Subscribers")
plt.title("Real time data")
plt.style.use('fivethirtyeight')
plt.show()