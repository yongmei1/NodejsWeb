import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle

# opening testing loan prediction dataset
testdf = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')

# Dropping the loan ID
testdf.drop('Loan_ID', axis=1, inplace=True)

# filling all the null data cells in the self employed column with no
testdf['Self_Employed'] = testdf['Self_Employed'].fillna('No')

# filling the empty data cells of LoanAmount with the mean amount
testdf['LoanAmount'] = testdf['LoanAmount'].fillna(testdf.LoanAmount.mean())

# drop any remaining empty rows
testdf.dropna(inplace=True)

# only including incomes lower than 50000 as the rest are outliers
testdf = testdf[testdf['ApplicantIncome'] < 50000]

# converting categorical data to numerical
testdf['Married'] = np.where((testdf['Married'] == 'Yes'), 1, 0)
testdf['Gender'] = np.where((testdf['Gender'] == 'Female'), 1, 0)
testdf['Education'] = np.where((testdf['Education'] == 'Graduate'), 1, 0)
testdf['Self_Employed'] = np.where((testdf['Self_Employed'] == 'Yes'), 1, 0)
testdf['Dependents'] = np.where((testdf['Dependents'] == '0'), 0, 1)

# label encoder is used here as there are more than 2 pieces of categorical data
# tried to use dictionaries and mapping first but had issues with conversion
le = preprocessing.LabelEncoder()
testdf['Property_Area'] = le.fit_transform(testdf['Property_Area'])

# selecting the file that contains the model.
filename = 'finalized_model.sav'

# using pickle to deserialize the model
loaded_model = pickle.load(open(filename, 'rb'))

# predicting the test data with model
pred = loaded_model.predict(testdf)

# printing the predictions
print(pred)

print("\n\nPredictions : "+pred[0])