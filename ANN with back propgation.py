import numpy as np import pandas as pd 
#import matplotlib.pyplot as plt 
 
dataset=pd.read_csv('heart.csv') 
 
x=dataset.iloc[:,[0,1,2,3,4,5,6,7,9,10,11,12]].values y=dataset.iloc[:,13:14].values 
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=2) 
 
 
from sklearn.preprocessing import StandardScaler sc=StandardScaler() x_train=sc.fit_transform(x_train) 
x_test=sc.fit_transform(x_test) 
 
import keras 
from keras.models import Sequential 
from keras.layers import Dense 
 
#NOTE 
'''If you are dealing with a dependent variable that has multiple categories say 3 and is onehotencoded, then activation function shall be softmax which is a sigmoid  function that deals with multiple categories''' 
 
classifier=Sequential() 
'''adding input layer and first hidden layer''' 
classifier.add(Dense(units=10, kernel_initializer='uniform', activation='relu', input_dim=12)) 
 
'''adding second hidden layer''' 
classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu')) 
 
'''adding the output layer''' 
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid')) 
'''compile the ANN''' 
#loss='categorical_crossentropy if there are multiple dependent variables' 
classifier.compile(optimizer='adagrad', loss='binary_crossentropy', metrics=['accuracy']) 
 
#fitting 
classifier.fit(x_train,y_train, batch_size=3, epochs=90) 
 
classifier1=classifier 
#prediction 
 
y_pred=classifier.predict(x_test) y_pred=np.around(y_pred) 
 
#confusion_matrix 
''' 
from sklearn.metrics import confusion_matrix cm=confusion_matrix(y_test,y_pred) 
acc=(cm[0][0]+cm[1][1])/(cm[0][1]+cm[1][0]+cm[0][0]+cm[1][1]) 
''' 
from sklearn.metrics import classification_report, confusion_matrix print(classification_report(y_test,y_pred)) 
 
from sklearn.externals import joblib 
 
filename = 'finalized_model_ann.sav' joblib.dump(classifier, filename) 
 
loaded_model = joblib.load(filename) 
test_vals=np.array([[ 57 ,   1 ,   0 , 130. , 131. ,   0. ,   1. , i[2] ,   1.2, 1. ,   1. ,   3 ]]) 
         
result = loaded_model.predict(test_vals)
result=np.around(result)
print(result) 
