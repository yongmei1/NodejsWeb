import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

traindf = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
testdf = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')

traindf.drop('Loan_ID', axis=1, inplace=True)
traindf['Self_Employed'] = traindf['Self_Employed'].fillna('No')
traindf['LoanAmount'] = traindf['LoanAmount'].fillna(traindf.LoanAmount.mean())
traindf.dropna(inplace=True)
testdf.drop('Loan_ID', axis=1, inplace=True)
testdf['Self_Employed'] = testdf['Self_Employed'].fillna('No')
testdf['LoanAmount'] = testdf['LoanAmount'].fillna(testdf.LoanAmount.mean())
testdf.dropna(inplace=True)

traindf = traindf[traindf['ApplicantIncome'] < 50000]
testdf = testdf[testdf['ApplicantIncome'] < 50000]

traindf['Married'] = np.where((traindf['Married'] == 'Yes'), 1, 0)
traindf['Gender'] = np.where((traindf['Gender'] == 'Female'), 1, 0)
traindf['Education'] = np.where((traindf['Education'] == 'Graduate'), 1, 0)
traindf['Self_Employed'] = np.where((traindf['Self_Employed'] == 'Yes'), 1, 0)
traindf['Dependents'] = np.where((traindf['Dependents'] == '0'), 0, 1)

testdf['Married'] = np.where((testdf['Married'] == 'Yes'), 1, 0)
testdf['Gender'] = np.where((testdf['Gender'] == 'Female'), 1, 0)
testdf['Education'] = np.where((testdf['Education'] == 'Graduate'), 1, 0)
testdf['Self_Employed'] = np.where((testdf['Self_Employed'] == 'Yes'), 1, 0)
testdf['Dependents'] = np.where((testdf['Dependents'] == '0'), 0, 1)

le = preprocessing.LabelEncoder()
traindf['Property_Area'] = le.fit_transform(traindf['Property_Area'])
testdf['Property_Area'] = le.fit_transform(testdf['Property_Area'])

y = traindf['Loan_Status']
X = traindf.drop('Loan_Status', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

LR = LogisticRegression(solver='lbfgs', max_iter=200)
LR.fit(X_train, y_train)

y_predict = LR.predict(X_test)

print(classification_report(y_test, y_predict))

LR_SC = accuracy_score(y_predict, y_test)
print('accuracy is', accuracy_score(y_predict, y_test))

pred = LR.predict(testdf)
print(pred)

