import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  
  
""" Importing Data """
  
data_sets = pd.read_csv('C:/Users/VARSHA/Cognizance/Task_6/Q2-Dataset.csv')
  
print ("Data Head : \n", data_sets.head())
  
print ("\n\nData Describe : \n", data_sets.describe())
  
""" Input and Output Data """
  
# All rows but all columns except last
X = data_sets.iloc[:, :-1].values
  
# TES
# All rows but only last column 
Y = data_sets.iloc[:, 3].values
                  
print("\n\nInput : \n", X)
print("\n\nOutput: \n", Y)
  
  
""" Handling the missing values """


from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = SimpleImputer(missing_values = "NaN",strategy = "mean")                 
# Fitting the data, function learns the stats
imputer = imputer.fit(X[:, 1:3])
  
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])
  
# filling the missing value with mean
print("\n\nNew Input with Mean Value for NaN : \n", X)