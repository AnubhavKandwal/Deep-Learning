#Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(<add_path>)

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

#creating the linear model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#training the model
regressor.fit(X_train, Y_train)

#predicting the test result
Y_pred = regressor.predict(X_test)

#plotting the predictions
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Train)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()