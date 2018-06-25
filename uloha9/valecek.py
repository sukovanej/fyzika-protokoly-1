import statistics
import math

R = [46.06, 46.10, 46.06, 46.06, 46.08, 46.06, 46.06, 46.06, 46.10, 46.08]
r = [9.80, 9.76, 9.78, 9.76, 9.82, 9.82, 9.72, 9.78, 9.80, 9.80]
h = [14.83, 14.75, 14.76, 14.77, 14.81, 14.82, 14.81, 14.86, 14.83, 14.77]

result = {}

student_6_6827 = 1.059
student_6_9973 = 4.094

student_5_6827 = 1.110
student_5_9973 = 5.507

student_9_6827 = 1.067
student_9_9973 = 4.094

for key, data in {"R": R, "r": r, "h": h}.items():
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    stdev1 = student_9_6827 * stdev
    stdev2 = student_9_9973 * stdev
    u = stdev1 / math.sqrt(len(data))
    r = stdev1 / mean * 100

    result[key] = {
        "mean": mean,
        "standard deviation": stdev,
        "standard deviation (0.6827)": stdev1,
        "standard deviation (0.9973)": stdev2,
        "u": u,
        "r": r
    }

print(result)
