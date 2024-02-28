import numpy as np
import matplotlib.pyplot as plt

men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']

x = np.arange(len(categories))

plt.figure(figsize=(10, 6))
plt.bar(x, men_means, yerr=men_std, capsize=5, label='Men', width=0.5, align='center', alpha=0.7)
plt.bar(x, women_means, yerr=women_std, capsize=5, label='Women', width=0.5, align='center', bottom=men_means, alpha=0.7)

plt.xlabel('Categories')
plt.ylabel('Means')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x, categories)
plt.legend()

plt.show()
