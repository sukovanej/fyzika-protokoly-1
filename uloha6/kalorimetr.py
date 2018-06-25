import math

m1 = 0.174631
t1 = 21.2
m2 = 0.178321
t2 = 72.6
t = 42.8
c = 4180

K = m2 * c * (t2 - t) * 1 / (t - t1) - m1 * c

ut = 0.1
um = 0.0000005

uK = math.sqrt(
    math.pow(c, 2) * math.pow(um, 2) +
    math.pow(c * (t2 - t) / (t - t1), 2) * math.pow(um, 2) +
    math.pow(c * m2 / (t - t1), 2) * math.pow(ut, 2) +
    math.pow(c * m2 * (t2 - t) / math.pow((t - t1), 2), 2) * math.pow(ut, 2) +
    math.pow(c * m2 * (t1 - t2) / math.pow((t - t1), 2), 2) * math.pow(ut, 2)
)

print("K = {} +- {}".format(K, uK))
