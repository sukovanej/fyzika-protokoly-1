import numpy
from math import pow, sqrt

pow2 = lambda x: x * x

data_raw = open('data3.txt').readlines()
data = list()
data_sub = list()

for line in data_raw:
    if line.strip() == '':
        data.append(data_sub)
        data_sub = []
    else:
        data_sub.append(float(line) + 273.15)

def calc_epsilon(t1_l: list, t2_l: list):
    t_1 = numpy.average(t1_l)
    t_1_err = numpy.average((t1_l - t_1)**2)
    t_2 = numpy.average(t2_l)
    t_2_err = numpy.average((t1_l - t_1)**2)

    epsilon = pow(t_1 / t_2, 4)
    epsilon_err = epsilon * sqrt(pow2(4 * t_1_err / t_1) + pow2(4 * t_2_err / t_2))
    return (epsilon, epsilon_err)

print(calc_epsilon(data[0], data[1]))
print(calc_epsilon(data[2], data[3]))
