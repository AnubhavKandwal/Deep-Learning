#import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv(<add_path>)

#creating matrix of features
X = dataset.iloc[:,0:3].values
Y = dataset.iloc[:,3].values

#print(X)
#print(Y)

#Handling missing data
from sklearn.impute import SimpleImputer
#taking mean for salary
imputer_mean = SimpleImputer(missing_values = np.nan, strategy = 'mean')
#taking median for age
imputer_median = SimpleImputer(missing_values = np.nan, strategy = 'median')
imputer_mean.fit(X[:,2:3])
imputer_median.fit(X[:,1:2])
X[:,2:3] = imputer_mean.transform(X[:,2:3])
X[:,1:2] = imputer_median.transform(X[:,1:2])


#Encode Categorical data

#Encode Independant Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

#Encode dependant Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(Y)


#Splitting Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

#print(X_train)
#print(X_test)
#print(Y_train)
#print(Y_test)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train[:,3:5] = ss.fit_transform(X_train[:,3:5])
X_test[:,3:5] = ss.transform(X_test[:,3:5])

#plotting the predictions
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
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