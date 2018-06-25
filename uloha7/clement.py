import numpy
h1 = [53, 68, 74, 107, 108, 123, 129, 154, 184, 193]
h2 = [1, 6, 7, 15, 16, 21, 23, 27, 34, 36]

kappa_list = list()

for i in range(len(h1)):
    kappa_list.append(h1[i] / (h1[i] - h2[i]))

kappa = numpy.average(kappa_list)
kappa_err = numpy.average((kappa_list - kappa)**2)

print(f"{kappa} +- {kappa_err}")
