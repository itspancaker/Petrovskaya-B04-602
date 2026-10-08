import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize=(16, 9))

ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)
axes = [ax1, ax2, ax3, ax4, ax5, ax6]

x_features = ['SepalLengthCm', 'SepalLengthCm', 'SepalLengthCm', 'SepalWidthCm', 'SepalWidthCm', 'PetalLengthCm']
y_features = ['SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'PetalWidthCm']

setosa = df[df['Species'] == 'Iris-setosa']
versicolor = df[df['Species'] == 'Iris-versicolor']
virginica = df[df['Species'] == 'Iris-virginica']

print("Коэффициенты прямых МНК (y = k * x + b):")

# Простой цикл от 0 до 5
for i in range(6):
    ax = axes[i]
    feat_x = x_features[i]
    feat_y = y_features[i]

    ax.scatter(setosa[feat_x], setosa[feat_y], color='red', label='Setosa' if i == 0 else "")
    ax.scatter(versicolor[feat_x], versicolor[feat_y], color='green', label='Versicolor' if i == 0 else "")
    ax.scatter(virginica[feat_x], virginica[feat_y], color='blue', label='Virginica' if i == 0 else "")

    k, b = np.polyfit(df[feat_x], df[feat_y], 1)
    x_line = np.linspace(df[feat_x].min(), df[feat_x].max(), 100)
    ax.plot(x_line, k * x_line + b, color='black', linestyle='--', label=f'МНК k={k:.2f}')

    print(f"График {i + 1} ({feat_y} от {feat_x}): k = {k:.3f}, b = {b:.3f}")

    ax.set_xlabel(feat_x)
    ax.set_ylabel(feat_y)
    ax.set_title(f'{feat_y} от {feat_x}')
    ax.grid(True)
    ax.legend(fontsize=9)

plt.tight_layout()
plt.show()