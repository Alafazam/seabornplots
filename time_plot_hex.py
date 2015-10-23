import __main__
import numpy as np
from scipy.stats import kendalltau
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

# rs = np.random.RandomState(11)
x = [17, 17, 17, 17, 17, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21, 21, 13, 23, 22, 22, 22, 22, 22, 22, 22, 20, 15, 19, 15, 14, 14, 14, 23, 19, 19, 23, 23, 21, 21, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 12, 12, 12, 23, 23, 23, 21, 21, 21, 21, 21, 23, 23, 22, 1, 12, 12, 12, 3, 2, 12, 23, 23, 23, 23, 23, 23, 23, 22, 15, 23, 23, 14, 14, 1, 1, 1, 12, 12, 12, 12, 12, 12, 12, 18, 18]
y = [30, 29, 29, 24, 19, 11, 9, 8, 7, 3, 57, 54, 52, 34, 30, 29, 8, 1, 49, 44, 33, 31, 29, 29, 28, 27, 2, 6, 5, 52, 41, 36, 18, 27, 26, 46, 32, 35, 33, 15, 14, 10, 0, 51, 49, 44, 43, 28, 27, 26, 19, 16, 56, 21, 19, 16, 49, 43, 39, 25, 23, 22, 21, 13, 23, 1, 13, 17, 59, 55, 54, 10, 59, 1, 59, 57, 27, 25, 22, 21, 4, 49, 59, 31, 30, 5, 0, 8, 6, 0, 39, 37, 35, 31, 27, 25, 18, 11, 9]

x = x+x+x+x+x+x+x+x+x+x
y = y+y+y+y+y+y+y+y+y+y


# print rs
# x = rs.gamma(12, size=60)
# y = 2 + rs.gamma(60,size=60)
# x = rs.gamma(2, size=1000)

# print type(y)
x = np.asarray(x)
y = np.asarray(y)


sns.jointplot(x, y, kind="hex", color="#4CB391")
# x = np.random.normal(size=100)
# print 'x = '+ str(x)
# graph = sns.distplot(x);


sns.plt.savefig(__main__.__file__+"3.png")
# graph.pyplot.show()
sns.plt.show()