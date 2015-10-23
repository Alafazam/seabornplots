import __main__
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "distributions")))
rs = np.random.RandomState(1000)
# x = rs.permutation(10)



mean, cov = [0, 1], [(1, .5), (.5, 1)]

data = np.random.multivariate_normal(mean, cov, 200)

df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df)

sns.plt.savefig(__main__.__file__+".png")
sns.plt.show()
