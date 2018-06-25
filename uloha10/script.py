from math import pow, sqrt, pi
import numpy

pow2 = lambda x: pow(x, 2)

U, uU = 36.2, 0.03
I, uI = 0.35, 0.005

t1, t2, t3, t4 = 82.5, 47.6, 32.1, 23.1
x1, x2, x3, x4 = 0.075, 0.203, 0.300, 0.414

ut = 0.05
ul = 0.0005

l = 0.500
d, ud = 0.0094, 0.00005
S, uS = pi * pow2(d / 2), pi * d * ud / 2


def calculate_lambda(dl, dT):
    lam = U * I * dl / (S * (dT + 273.15))
    ulam = lam * sqrt(pow2(uU / U) + pow2(uI / I) + pow2(uS / S) + pow2(ul / dl)
                      + pow2(ut / dT))

    return (lam, ulam)


results = list()

results.append(calculate_lambda(x2 - x1, t1 - t2)[0])
results.append(calculate_lambda(x3 - x1, t1 - t3)[0])
results.append(calculate_lambda(x4 - x1, t1 - t4)[0])
results.append(calculate_lambda(x3 - x2, t2 - t3)[0])
results.append(calculate_lambda(x4 - x2, t2 - t4)[0])
results.append(calculate_lambda(x4 - x3, t3 - t4)[0])

errs = list()

errs.append(calculate_lambda(x2 - x1, t1 - t2)[1])
errs.append(calculate_lambda(x3 - x1, t1 - t3)[1])
errs.append(calculate_lambda(x4 - x1, t1 - t4)[1])
errs.append(calculate_lambda(x3 - x2, t2 - t3)[1])
errs.append(calculate_lambda(x4 - x2, t2 - t4)[1])
errs.append(calculate_lambda(x4 - x3, t3 - t4)[1])

result = numpy.average(results)
err = numpy.average(errs)

print(f"{result} +- {err}")
