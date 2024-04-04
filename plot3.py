# -*- coding: utf-8 -*-
"""Plot3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15X0S7bk6ThpS-C8M6KQiWYhM5cGkiBKs
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv("/content/household_power_consumption.txt",
                   sep=";",
                   na_values=["?"],
                   parse_dates={'DateTime': ['Date', 'Time']},
                   keep_date_col=True,
                   dayfirst=True)
data = data[(data['DateTime'] >= '2007-02-01') & (data['DateTime'] <= '2007-02-02')]

data['datetime'] = pd.to_datetime(data['DateTime'], format='%d/%m/%Y %H:%M:%S')

plt.figure(figsize=(6, 6))
plt.plot(data['datetime'], data['Sub_metering_1'], label='Sub_metering_1', color='black')
plt.plot(data['datetime'], data['Sub_metering_2'], label='Sub_metering_2', color='red')
plt.plot(data['datetime'], data['Sub_metering_3'], label='Sub_metering_3', color='blue')

plt.xlabel('Date and Time')
plt.ylabel('Energy sub metering')
plt.title('Energy Sub Metering')

plt.legend(loc='upper right')