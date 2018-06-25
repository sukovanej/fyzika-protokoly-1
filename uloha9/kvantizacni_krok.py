import numpy
import matplotlib.pyplot as plt

data = numpy.loadtxt("data.txt")
data_diffs = []

for i in range(len(data)):
    if i == 0:
        continue

    data_diffs.append(abs(data[i] - data[i - 1]))

data_sorted = numpy.unique(numpy.sort(data_diffs))

print(data_sorted[:20])

plt.plot(data_sorted, 'ro')
plt.savefig("diffs.png")
