import numpy
from math import pow, sqrt

pow2 = lambda x: x * x

data = [
    (961.7, [24.0, 41.7, 59.6, 77.5, 95.5]),
    (1255.1, [33.0, 46.7, 60.2, 74., 87.8, 101.5]),
    (1500.6, [24.3, 36.0, 47.5, 58.6, 70.2, 81.6, 93.0, 104.5]),
    (1765.4, [29.1, 39.0, 48.5, 58.4, 68.0, 77.8, 87.5, 97.3, 107.0]),
    (2012.1, [22.0, 30.8, 40.5, 49.2, 57.6, 65.8, 74.6, 83.2, 91.8, 100.3, 108.9])
]

rho, urho = 1.129, 0.001
p, up = 96650, 50
uf = 0.1

def calc_lambda(x: list):
    last = x[0]
    l = list()

    for i in range(1, len(x)):
        l.append((x[i] - last) * 1e-2) # cm -> m
        last = x[i]

    x_average = numpy.average(l)
    x_err = numpy.average((l - x_average)**2)

    return (2 * x_average, 2 * x_err)

def calc_kappa(lam, f):
    kappa = pow(lam[0] * f, 2) * rho / p
    kappa_err = kappa * sqrt(pow2(2 * uf / f) + pow2(2 * lam[1] / lam[0]) + pow2(up / p) + pow2(urho / rho))

    return (round(kappa, 3), round(kappa_err, 3))

for d in data:
    lam = calc_lambda(d[1])
    print(calc_kappa(lam, d[0]))
