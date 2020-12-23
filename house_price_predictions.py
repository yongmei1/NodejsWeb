import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import pickle

# opening the csv that contains the house price data
df = pd.read_csv('kc_house_data.csv')

# dropping id, zipcode, date, lat, and long as they the either they arent relevant or they are too specific to the area
# the house prices come from (king county)
df = df.drop(['id', 'zipcode', 'date', 'lat', 'long'], axis=1)


# scaler being used
scaler = MinMaxScaler()

# selecting the file that contains the model.
filename = 'seq_model.sav'

# using pickle to deserialize the model
loaded_model = pickle.load(open(filename, 'rb'))

# getting the first row from the dataset and comparing its price with predicted price
single_house = df.drop('price', axis=1).iloc[0]
print(f'Features of new house:\n{single_house}')

single_house = scaler.transform(single_house.values.reshape(-1, 15))

print('\nPrediction Price:', loaded_model.predict(single_house)[0, 0])

print('\nOriginal Price:', df.iloc[0]['price'])
