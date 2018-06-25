from math import pow, sqrt, pi

pow2 = lambda x: pow(x, 2)

R = 46.07 / 1000
r = 9.78 / 1000
h = 14.80 / 1000
m = 191.5761 / 1000

uR = 0.01 / 1000
ur = 0.01 / 1000
uh = 0.01 / 1000
um = 0.00005 / 1000

u = 4 / (pi * h * (pow2(R) - pow2(r))) * \
        sqrt(pow2(um) + pow2(m * uh / h) + pow2(2 * R * m * uR / (pow2(R) - \
        pow2(r))) + pow2(2 * r * m * ur / (pow2(R) - pow2(r))))


rho = m / (pi * h * (pow2(R / 2) - pow2(r / 2)))

print("({} +- {}) kg * m^-3".format(rho, u))
