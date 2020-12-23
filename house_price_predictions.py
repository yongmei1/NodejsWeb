import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# opening the csv that contains the house price data
df = pd.read_csv('kc_house_data.csv')

# dropping id, zipcode, date, lat, and long as they the either they arent relevant or they are too specific to the area
# the house prices come from (king county)
df = df.drop(['id', 'zipcode', 'date', 'lat', 'long'], axis=1)

# features
X = df.drop('price', axis=1)

# target
y = df['price']

# splitting the data set into training an testing, testing being 1/3 of the data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=54)

# scaler being used
scaler = MinMaxScaler()

# fitting the data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# using the sequential model
Seq = Sequential()

# setting up the neural network layers
Seq.add(Dense(16, activation='relu'))

Seq.add(Dense(16, activation='relu'))
Seq.add(Dense(16, activation='relu'))
Seq.add(Dense(16, activation='relu'))

Seq.add(Dense(1))

# compile the model using adam and mse
Seq.compile(optimizer='adam', loss='mse')

# fitting the data, and setting the batch size and number of epochs
Seq.fit(x=X_train, y=y_train.values,
        validation_data=(X_test, y_test.values),
        batch_size=1024, epochs=400)


# testing the data
predict = Seq.predict(X_test)
print(classification_report(y_test, predict))
print('accuracy is', accuracy_score(predict, y_test))

# getting the first row from the dataset and comparing its price with predicted price
single_house = df.drop('price', axis=1).iloc[0]
print(f'Features of new house:\n{single_house}')

single_house = scaler.transform(single_house.values.reshape(-1, 15))

print('\nPrediction Price:', Seq.predict(single_house)[0, 0])

print('\nOriginal Price:', df.iloc[0]['price'])
