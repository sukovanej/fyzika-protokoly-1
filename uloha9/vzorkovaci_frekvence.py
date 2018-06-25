import matplotlib.pyplot as plt
import numpy

freq = 3
f = 6

step = 1.0 / f

data = [numpy.sin(freq * x) for x in numpy.arange(0, 20, step)]

plt.plot(data)
plt.savefig("freq_3.png")
