# https://www.youtube.com/watch?v=_LWjaAiKaf8
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
import pandas as pd

date_format = mpl_dates.DateFormatter("%d %b %Y")
data = pd.read_csv("C:/OtherProjects/Learning-MatPlotLib/08 - Plotting Time Series Data/Data.csv")
data["Date"] = pd.to_datetime(data["Date"])
# data.sort_values("Date", inplace=True) # Sort the data by the date field
price_date = data["Date"]
price_close = data["Close"]

plt.plot_date(price_date, price_close, linestyle="solid")
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Bitcoin price (USD) over time")
plt.xlabel("Date")
plt.ylabel("Bitcoin price (USD)")
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.savefig("C:/OtherProjects/Learning-MatPlotLib/08 - Plotting Time Series Data/Time Series Data.png")
plt.show()