from scipy import stats

data_raw = open('mereni_8_000.txt').readlines()
x = list()
y = list()

for line in data_raw:
    d = line.replace(',' ,'.').split('\t')
    x.append(float(d[1]))
    y.append(float(d[4]))

b, a, _, _, err = stats.linregress(x, y)
alpha = b / a

print(f"R_0 = {a}")
print(f"alpha = {alpha} +- {err}")
