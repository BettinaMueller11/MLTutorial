import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import pickle
import os

df = pd.read_csv(os.path.join('data', 'auto-mpg.csv'),sep=";")
print(df.head())
print(df.columns)

# Define target
y = df['mpg']

# Define predictors
X = df[['ps', 'gewicht']]

# Define test and training data
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, y, test_size=test_size, random_state=seed)


# Fit linear regression model on training set
model = LinearRegression()
model.fit(X_train, Y_train)

y_pred=model.predict(X_train)


# Save the model to disk
filename = open('data/models/models.pickle','wb')
