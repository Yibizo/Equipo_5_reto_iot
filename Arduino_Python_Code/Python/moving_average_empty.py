import matplotlib.pyplot as plt
import random
import pandas as pd


def smooth_curve_average(points, sample_size):
    #smoothed_points = pd.DataFrame(points).sum(axis=1).rolling(sample_size, min_periods=1).mean()
    smoothed_points = []
    for i in range(1, len(points)+1):
        if i > sample_size:
            smoothed_points.append(sum(points[i-sample_size:i])/sample_size)
        else:
            smoothed_points.append(sum(points[:i])/i)

    return smoothed_points


def smooth_curve_exponential(points, factor=0.9):
    #smoothed_points = pd.DataFrame(points).sum(axis=1).ewm(alpha=factor, adjust=False).mean()
    smoothed_points = []
    for i in range(len(points)):
        if i > 0:
            smoothed_points.append(factor*points[i] + (1-factor)*points[i-1])
        else:
            smoothed_points.append(points[i])

    return smoothed_points

sample_size = 20
data_series = []
peaks = []

random.seed(0)

while len(data_series) < 1000:
    data_series.append(random.uniform(360, 380))

data_series_smooth_ex = smooth_curve_exponential(data_series, 0.95)
data_series_smooth_av = smooth_curve_average(data_series, 20)


plt.plot(data_series)
plt.plot(data_series_smooth_ex)
plt.plot(data_series_smooth_av)
plt.ylabel("Data")
plt.show()


