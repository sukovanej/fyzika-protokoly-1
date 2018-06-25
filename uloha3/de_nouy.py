import sys
import numpy
import matplotlib.pyplot as plt

file_name = sys.argv[1]
data = numpy.loadtxt(file_name)

x = [i[0] for i in data]
y = [i[1] for i in data]

plt.plot(x, y)
plt.savefig(f"{file_name}.png")
print(max(y))
