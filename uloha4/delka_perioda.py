from matplotlib import pyplot as plt
import numpy as np

datax_1 = [5.634, 6.094, 11.214, 12.978]
datay_1 = [0.98312, 0.98902, 1.0054, 1.0127]

datax_2 = [12.996, 10.814, 8.128, 6.696, 5.552]
datay_2 = [1.0815, 1.0321, 0.97918, 0.95602, 0.93798]

plt.plot(datax_1, datay_1)
plt.plot(datax_2, datay_2)

plt.savefig('delka_perioda.png')
