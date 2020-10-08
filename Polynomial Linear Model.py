#importing the modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(<add_path>)
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
Lregressor = LinearRegression()
Lregressor.fit(X, Y)

from sklearn.preprocessing import PolynomialFeatures
features = PolynomialFeatures(degree = 2)
X_feature = features.fit_transform(X)
Lregressor2 = LinearRegression()
Lregressor2.fit(X_feature, Y)

features = PolynomialFeatures(degree = 3)
X_feature2 = features.fit_transform(X)
Lregressor3 = LinearRegression()
Lregressor3.fit(X_feature2, Y)

features = PolynomialFeatures(degree = 4)
X_feature3 = features.fit_transform(X)
Lregressor4 = LinearRegression()
Lregressor4.fit(X_feature3, Y)

#plotting graph
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, Y, color = 'red')
plt.plot(X, Lregressor.predict(X), color = 'blue')
plt.title('Linear Plot')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

plt.plot(X, Lregressor2.predict(X_feature), color = 'green')
plt.title('Polynomial Plot')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

plt.plot(X, Lregressor3.predict(X_feature2), color = 'purple')
plt.title('Polynomial Plot')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

plt.plot(X, Lregressor4.predict(X_feature3), color = 'yellow')
plt.title('Polynomial Plot')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

#prediction for 6.5 years
print(Lregressor.predict(np.array([[6.5]])))
print(Lregressor4.predict(features.fit_transform([[6.5]])))
