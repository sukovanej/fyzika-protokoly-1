from numpy import exp
from scipy.optimize import curve_fit

data_raw = open('suk_mereni_000.txt').readlines()
x = list()
y = list()

for line in data_raw:
    d = line.replace(',' ,'.').split('\t')
    x.append(float(d[0]))
    y.append(float(d[1]) + 273.15)

def func(x, a, b, c):
    return a + b * exp(- x / c)

popt, pcov = curve_fit(func, x, y)

print(popt)
