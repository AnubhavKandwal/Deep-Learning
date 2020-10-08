#importing required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv(<add_path>)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values

#encode the categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

#Test-Train Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, train_size = 0.8, random_state = 0)

#multiple linear model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
np.set_printoptions(precision = 2)
print(np.concatenate((Y_pred.reshape(len(Y_pred), 1), Y_test.reshape(len(Y_pred), 1)), axis = 1))

#to predict particular values
print(regressor.predict([[1,0,0,160000,130000,300000]]))

#to find coefficients and intercept for an equations
print(regressor.coef_)
print(regressor.intercept_)

#181566.92

pred = ((86.6*1)-(873*0)+(786*0)+(0.773*160000)+(0.0329*130000)+(0.0366*300000)+42467.52924854249)
