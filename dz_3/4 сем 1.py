import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x_measured = [70, 80, 85, 100, 115, 150, 195, 260, 415, 480]
y_measured = [236, 250, 276, 313, 396, 466, 619, 830, 1280,1650]

k, b = np.polyfit(x_measured, y_measured, 1)

x_mnk = np.linspace(min(x_measured), max(x_measured), 100)
y_mnk = k * x_mnk + b

ax1.scatter(x_measured, y_measured, marker='x')

ax1.errorbar(x_measured, y_measured, yerr=0.01, xerr = 2.5, color = 'k', linestyle = 'None')

ax1.plot(x_mnk, y_mnk, 'r-', linewidth=2, label=f'МНК: y = {k:.3f}x + ({b:.3f})')

ax1.grid()
ax1.set_title('Зависимость показаний вольметра от показаний амперметра для нихромовой проволоки длиной 30 см')
plt.show()
