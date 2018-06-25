#!/usr/local/bin/python3
import numpy
import matplotlib.pyplot as plt
from scipy import stats

data = [float(i.strip()) for i in open('data_1').readlines()[:21]]
weights = [float(i.strip()) for i in open('vahy_1').readlines()[:10]]

x = list()
last = 0
for i in weights:
    last = last + i
    x.append(last)

x.insert(0, 0)

x_rev = list(reversed(x))

y = data[:11]
y_rev = data[10:]

# print(x, '\n', x_rev, len(x), len(x_rev))
# print(y, '\n', y_rev, len(y), len(y_rev))

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(slope, std_err)
slope, intercept, r_value, p_value, std_err = stats.linregress(x_rev, y_rev)
print(slope, std_err)
