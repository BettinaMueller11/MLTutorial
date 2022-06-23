
import pickle
import os
import pandas as pd

#Load model
file_to_open = open('data/models/models.pickle', 'rb')

trained_model = pickle.load(file_to_open)
file_to_open.close()

# Prediction
prediction_data = pd.read_csv(os.path.join('data', 'predictiondata.csv'),sep=";")

print(trained_model.predict(prediction_data))
