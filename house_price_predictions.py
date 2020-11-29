import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv('kc_house_data.csv')
df = df.drop(['id', 'zipcode', 'date', 'lat', 'long'], axis=1)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=54)

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print('Max: ', X_train.max())
print('Min: ', X_train.min())

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print('Max: ', X_train.max())
print('Min: ', X_train.min())

model = Sequential()

model.add(Dense(16, activation='relu'))

model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))

model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

model.fit(x=X_train, y=y_train.values,
          validation_data=(X_test, y_test.values),
          batch_size=128, epochs=400)

predictions = model.predict(X_test)

print(predictions)

# features of new house
single_house = df.drop('price', axis=1).iloc[0]
print(f'Features of new house:\n{single_house}')

# reshape the numpy array and scale the features
single_house = scaler.transform(single_house.values.reshape(-1, 15))

# run the model and get the price prediction
print('\nPrediction Price:', model.predict(single_house)[0, 0])

# original price
print('\nOriginal Price:', df.iloc[0]['price'])
