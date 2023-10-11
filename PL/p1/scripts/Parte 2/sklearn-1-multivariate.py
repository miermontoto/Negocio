import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
X_full = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
Y = raw_df.values[1::2, 2]
print(raw_df.columns)

print(X_full.shape)
print(Y.shape)
X = X_full[:, :]
orden = np.argsort(Y)
horizontal = np.arange(Y.shape[0])
plt.scatter(horizontal, Y[orden], color='black')

regressor = LinearRegression()
regressor.fit(X, Y)
plt.scatter(horizontal, regressor.predict(X)[orden], 2, color='blue')

regressor = SVR(kernel='rbf', C=1e5, epsilon=1)
regressor.fit(X, Y)
plt.scatter(horizontal, regressor.predict(X)[orden], 2, color='green')

regressor = RandomForestRegressor()
regressor.fit(X, Y)
plt.scatter(horizontal, regressor.predict(X)[orden], 2, color='red')

regressor = MLPRegressor()
regressor.fit(X, Y)
plt.scatter(horizontal, regressor.predict(X)[orden], 2, color='yellow')

plt.legend(['Real', 'Linear', 'SVR', 'Random Forest', 'MLP'])
plt.show()
