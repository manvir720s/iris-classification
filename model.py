# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Importing the dataset
data = pd.read_csv('iris.csv')

# Dictionary containing the mapping
variety_mappings = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# Encoding the target variables to integers
data = data.replace(['Setosa', 'Versicolor' , 'Virginica'],[0, 1, 2])

data = data.drop(data.columns[0], axis = 1)
X = data.iloc[:, 0:-1] # Extracting the independent variables
y = data.iloc[:, -1] # Extracting the target/dependent variable
print(X.head())
print(y.head())

logreg = LogisticRegression() # Initializing the Logistic Regression model
logreg.fit(X, y) # Fitting the model

# Function for classification based on inputs
def classify(a, b, c, d):
    arr = np.array([a, b, c, d]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # Reshape the array
    prediction = logreg.predict(query)[0] 
    return prediction # Return the prediction
