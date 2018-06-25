import numpy as np
import sys

file_data = np.loadtxt(sys.argv[1])

m = 0.174631
c = 4180
K = 290

t_0 = 21
t_p = file_data[0][1]

y = [x[1] for x in file_data]
y_log = [np.log(x[1] - t_0) for x in file_data]
x = [x[0] * 60 for x in file_data]

fit = np.polyfit(x, y_log, 1)
beta = - fit[0] * (m * c + K)

print("beta = ", beta)

import matplotlib.pyplot as plot

prediction_x = x
prediction_y = [np.exp(fit[0] * t) * np.exp(fit[1]) + t_0 for t in x]

fig, plots = plot.subplots()

plots.plot(x, y, 'r--', label="naměřeno")
plots.plot(prediction_x, prediction_y, 'b--', label="model")

plot.legend()
plot.ylabel("teplota [C]")
plot.xlabel("čas [s]")
plot.savefig(sys.argv[1].split('.')[0] + '.png')
