#!/usr/local/bin/python3
import numpy
import matplotlib.pyplot as plt
from scipy import stats


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


data_raw = [float(i.strip()) * 1e-3 for i in open('data_2').readlines() if is_number(i)]
weights = [float(i.strip()) * 1e-3 for i in open('vahy_2').readlines()[:10]]
sizes = [float(i.strip()) * 1e-3 for i in open('data_2_rozmery').readlines() if is_number(i)]

a, ua, b, ub = list(), list(), list(), list()

for i in range(5):
    a.append(numpy.average(sizes[20 * i : 20 * i + 10]))
    b.append(numpy.average(sizes[20 * i + 10 : 20 * i + 20]))

    ub.append(numpy.average((sizes[20 * i : 20 * i + 10] - a[-1])**2))
    ua.append(numpy.average((sizes[20 * i + 10 : 20 * i + 20] - b[-1])**2))

data_points = [(0, 9), (9, 30), (30, 51), (51, 72), (72, 93)]
data = list()
for i, j in data_points:
    data.append(data_raw[i:j])

_x = list()
_x.append(0)
last = 0
for i in weights:
    last = last + i
    _x.append(last)

x = [_x[:5]]
for _ in range(4):
    x.append(_x)


def analyze(x, y):
    x_rev = list(reversed(x))
    k1, _, _, _, err1 = stats.linregress(x, y[:len(x)])
    k2, _, _, _, err2 = stats.linregress(x_rev, y[len(x) - 1:])
    return (k1, err1, k2, err2)


def calculate_e(a, ua, b, ub, l, ul, k, uk):
    from math import pow, sqrt
    g = 9.81
    pow2 = lambda x: pow(x, 2)
    E = g * pow(l, 3) / (4 * k * pow(a, 3) * b)
    uE = g * pow(l, 3) / (4 * k * pow(a, 3) * b) * sqrt(pow2(3 * ua / a) + pow2(ub / b) +
                                                        pow2(3 * ul / l) + pow2(uk / k))

    return (E, uE)


l, ul = (0.898, 0.0005)
for i in range(5):
    k1, uk1, k2, uk2 = analyze(x[i], data[i])
    print(calculate_e(a[i], ua[i], b[i], ub[i], l, ul, k1, uk1))
    print(calculate_e(a[i], ua[i], b[i], ub[i], l, ul, k2, uk2))
