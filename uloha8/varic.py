import numpy
from math import pow, sqrt

pow2 = lambda x: x * x

data_initial_raw = [float(i) + 273.15 for i in open('data1.txt').readlines()[:10]]
data_raw = open('data1.txt').readlines()
data = list()
data_sub = list()

T = numpy.average(data_initial_raw)
uT = numpy.average((data_initial_raw - T)**2)

T = 210 + 273.15
uT = 0.1

for line in data_raw:
    if line.strip() == '':
        data.append(data_sub)
        data_sub = []
    else:
        data_sub.append(float(line) + 273.15)

def calc_epsilon(d: list):
    t_p = numpy.average(d)

    epsilon = pow(t_p / T, 4)
    epsilon_err = epsilon * sqrt(pow2(4 * uT / T))

    return (epsilon, epsilon_err)

for d in data:
    print(calc_epsilon(d))
