import __main__
import numpy as np
from scipy.stats import kendalltau
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

rs = np.random.RandomState(1000)
x = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 1, 11, 10, 10, 10, 10, 10, 10, 10, 8, 3, 7, 3, 2, 2, 2, 11, 7, 7, 11, 11, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 12, 12, 12, 11, 11, 11, 9, 9, 9, 9, 9, 11, 11, 10, 1, 12, 12, 12, 3, 2, 12, 11, 11, 11, 11, 11, 11, 11, 10, 3, 11, 11, 2, 2, 1, 1, 1, 12, 12, 12, 12, 12, 12, 12, 6, 6]
y = [30, 29, 29, 24, 19, 11, 9, 8, 7, 3, 57, 54, 52, 34, 30, 29, 8, 1, 49, 44, 33, 31, 29, 29, 28, 27, 2, 6, 5, 52, 41, 36, 18, 27, 26, 46, 32, 35, 33, 15, 14, 10, 0, 51, 49, 44, 43, 28, 27, 26, 19, 16, 56, 21, 19, 16, 49, 43, 39, 25, 23, 22, 21, 13, 23, 1, 13, 17, 59, 55, 54, 10, 59, 1, 59, 57, 27, 25, 22, 21, 4, 49, 59, 31, 30, 5, 0, 8, 6, 0, 39, 37, 35, 31, 27, 25, 18, 11, 9]

# print rs
# x = rs.gamma(12, size=60)
# y = 2 + rs.gamma(60,size=60)
# x = rs.gamma(2, size=1000)

# print 'y = '+ str(y)

graph = sns.jointplot(x, y, kind="hex", stat_func=kendalltau, color="#4CB391")


# x = np.random.normal(size=100)
# print 'x = '+ str(x)
# graph = sns.distplot(x);


sns.plt.savefig(__main__.__file__+".png")
# graph.pyplot.show()
sns.plt.show()