import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')
print(df)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

counts = df['Species'].value_counts()
ax1.pie(counts, labels=counts.index, autopct='%1.1f%%')
ax1.set_title('Соотношение видов ирисов')

x = sum(df['PetalLengthCm'] <= 1.2)
y = sum((df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] < 1.5))
z = sum(df['PetalLengthCm'] >= 1.5)
ax2.pie([x, y, z], labels=['≤ 1.2 см', '1.2 до 1.5 см', '≥ 1.5 см'], autopct='%1.1f%%')
ax2.set_title('Распределение длины лепестков среди ирисов')

plt.show()