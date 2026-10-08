import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(16, 9))  # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(311)  # создали Axes (подграфик) ax1 в серии из 3 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

# сгенерируем данные для какой-нибудь гистограммы
values1 = np.random.normal(0, 10, 1000)
values2 = np.random.normal(0, 10, 5000)
values3 = np.random.normal(0, 10, 100000)


# строим гистограмму с 100 блоками
ax1.hist(values1, 100)
ax1.grid()
ax1.set_title('1000 точек')

ax2.hist(values2, 100)
ax2.grid()
ax2.set_title('5000 точек')

ax3.hist(values3, 100)
ax3.grid()
ax3.set_title('100000 точек')

plt.show()
