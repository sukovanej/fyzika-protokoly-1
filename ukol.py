import statistics
import math
from scipy import stats

data = [60.754, 58.844, 63.213, 62.885, 55.793, 58.406]

result = {}

student_6_6827 = 1.059
student_6_9973 = 4.094

student_5_6827 = 1.110
student_5_9973 = 5.507

result["mean"] = statistics.mean(data)
result["standard deviation"] = statistics.stdev(data)
result["standard deviation (0.6827)"] = \
        student_5_6827 * result["standard deviation"]
result["standard deviation (0.9973)"] = \
        student_5_9973 * result["standard deviation"]
result["u"] = \
        result["standard deviation (0.6827)"] / math.sqrt(len(data))
result["relative error"] = \
        result["standard deviation (0.6827)"] / result["mean"] * 100

print(result)
