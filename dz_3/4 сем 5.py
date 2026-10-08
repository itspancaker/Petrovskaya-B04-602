import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])

data = df['time']
price = df['close']

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(111)

ax1.plot(data, price, linewidth=2)

ticks_positions = pd.to_datetime(['2018-01-01', '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01'])
ax1.set_xticks(ticks_positions)

ticks_text = ['01-01-2018', '01-01-2019', '01-01-2020', '01-01-2021', '01-01-2022', '01-01-2023']

ax1.set_xticklabels(ticks_text)

ax1.grid(True)
ax1.set_title('График цены Биткоина')

plt.show()