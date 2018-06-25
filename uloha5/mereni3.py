import numpy
from math import pi, sqrt, pow

m = 5.905
um = 0.0005
_T = [3.96, 3.99, 4.07, 3.99, 3.99, 4.07, 4.02, 3.99, 3.96, 3.91] # s
_R = [9.576, 9.562, 9.562, 9.572, 9.560, 9.524, 9.570, 9.578, 9.514, 9.568] # cm
_l = [51.5, 51.4, 51.6, 51.4, 51.5, 51.5, 51.4, 51.5, 51.4, 51.6] # cm
_r = [1.00, 1.00, 0.99, 1.00, 1.00, 0.99, 0.99, 1.00, 0.99, 1.00] # mm

# uprava na zakladni jednotky
_R = [i * 1e-2 for i in _R]
_l = [i * 1e-2 for i in _l]
_r = [i * 1e-3 for i in _r]

T = numpy.average(_T)
R = numpy.average(_R)
l = numpy.average(_l)
r = numpy.average(_r)

uT = numpy.average((_T - T)**2)
uR = numpy.average((_R - R)**2)
ul = numpy.average((_l - l)**2)
ur = numpy.average((_r - r)**2)

pow2 = lambda x: pow(x, 2)
G = 16 * pi * m * pow(R, 2) * l / (5 * pow(r, 4) * pow(T, 2))
uG = G * sqrt(pow2(um /m) + pow2(2 * uR / R) + pow2(ul / l) + pow2(4 * ur / r) + pow2(2 * uT / T))

print(G, uG)
