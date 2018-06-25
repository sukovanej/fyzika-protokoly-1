import matplotlib.pyplot as plt
from scipy import stats
import numpy

R_V = 100000
R_A = 1800

def add(filename, curve_type):
    data = numpy.loadtxt(filename, delimiter=';')

    data_x = [x[0] * 0.001 for x in data]
    data_y = [x[1] for x in data]

    for i in range(len(data_x)):
        data_x[i] = data_x[i] + data_y[i] / R_V

    slope, intercept, r_value, p_value, std_err = stats.linregress(
        data_x, data_y)

    regression_x = data_x
    regression_y = [slope * x + intercept for x in regression_x]

    print("{filename}: R = {val} +- {std_err}".format(
        filename=filename, val=slope, std_err=std_err))

    plt.plot(data_x, data_y, curve_type)
    plt.plot(regression_x, regression_y, '-')

if __name__ == '__main__':
    add("A__1", 'ro')
    add("A__2", 'ro')

    #plt.ylabel('Napeti [V]')
    #plt.xlabel('Proud [A]')
    #plt.savefig('B.png')
