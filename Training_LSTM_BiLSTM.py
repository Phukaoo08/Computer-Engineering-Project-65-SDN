# Imported library 

import numpy as np
import pandas as pd
import tensorflow as tf
import keras as kf
from keras.wrappers.scikit_learn import KerasClassifier
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#------------------------------------------------------------------------------------------------
# Import CSV file, Scailing Data and config train-test.

df = pd.read_csv('Network_Analytics.csv', index_col='Timestamp')
print(df.shape[0])
scaler = MinMaxScaler(feature_range=(0, 1))
df = df[5000:15000] 
train, test = train_test_split(df, test_size=0.20, shuffle=False)
train = scaler.fit_transform(train)
test = scaler.fit_transform(test)
print(train.shape)

#------------------------------------------------------------------------------------------------

step = 32
space = 1
k_train = train.shape[0] - step

k_test = test.shape[0] - step

# Create Input and output Slice
x_train = np.array([train[i: i + step] for i in range(0, k_train, space)])
y_train = np.array([train[i + step: i + step + 1] for i in range(0, k_train, space)])
print(x_train.shape)
print(x_train[0].shape)
print('--------------')
x_test = np.array([test[i: i + step] for i in range(0, k_test, space)])
y_test = np.array([test[i + step: i + step + 1] for i in range(0, k_test, space)])

#------------------------------------------------------------------------------------------------

from keras import backend as K

# RMSE
def root_mean_squared_error(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true))) 

# MAE
def mean_absolute_error(y_true, y_pred):
    return K.mean(K.abs(y_pred - y_true))

#------------------------------------------------------------------------------------------------
# LSTM Training 

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-6)
model = Sequential()
# model.add(Embedding(n_unique_words, 128, input_length=maxlen))
model.add(LSTM(32,input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32,activation='relu', return_sequences=True))
model.add(Dropout(0.2))
# model.add(Dense(64, activation='tanh'))
# model.add(Dropout(0.2))
# model.add(Dense(64, activation='tanh'))
# model.add(Dropout(0.2))
model.add(Dense(1, activation='relu'))
model.compile(loss= mean_absolute_error, optimizer= 'rmsprop')

#------------------------------------------------------------------------------------------------
# LSTM Result with batch size and epochs

history=model.fit(x_train, y_train,
           batch_size=64,
           epochs=100,
           validation_data=[x_test, y_test])
print(history.history['loss'])

#------------------------------------------------------------------------------------------------
# LSTM Graph

from matplotlib import pyplot
pyplot.plot(history.history['loss'],label="loss", color='c')
pyplot.title('model MAE/epoch 5/LSTM/batchSize 32/step 100')
pyplot.xlabel('epoch')
pyplot.ylabel('Error %')
pyplot.xlim([0.00, 4.00])
pyplot.legend(loc='upper right')
pyplot.show() 

#------------------------------------------------------------------------------------------------
# Bi-LSTM Training 

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-6)

model1 = Sequential()
#model.add(Embedding(n_unique_words, 128, input_length=maxlen))
#model.add(Embedding(n_unique_words, 128, input_length=maxlen))
model1.add(Bidirectional(LSTM(32, input_shape=(x_train.shape[1:]), activation='relu',return_sequences=True)))
model1.add(Dropout(0.2))
#model.add(Bidirectional(LSTM(30, activation='relu', return_sequences=True)))
model1.add(Bidirectional(LSTM(32, activation='relu',return_sequences=True)))
model1.add(Dropout(0.2))
#model.add(Bidirectional(LSTM(10, activation='relu')))
# model1.add(Dense(25, activation='relu'))
# model1.add(Dropout(0.2))
model1.add(Dense(1, activation='relu'))
model1.compile(loss= mean_absolute_error, optimizer= 'rmsprop')


#------------------------------------------------------------------------------------------------
# Bi-LSTM Result with batch size and epochs

history=model1.fit(x_train, y_train,
           batch_size=64,
           epochs=100,
           validation_data=[x_test, y_test])
print(history.history['loss'])

#------------------------------------------------------------------------------------------------
# Bi-LSTM Graph
from matplotlib import pyplot
pyplot.plot(history1.history['loss'],  label="loss", color="r")
pyplot.title('model MAE/epoch 5/BiLSTM/batchSize 32/step 100')
pyplot.xlabel('epoch')
pyplot.ylabel('Error %')
pyplot.xlim([0.00, 4.00])
# pyplot.ylim([0.00, 0.25])
pyplot.legend(loc='upper right')
pyplot.show()

#------------------------------------------------------------------------------------------------
# Comparing between LSTM and Bi-LSTM
from matplotlib import pyplot
pyplot.plot(history.history['loss'],label="loss", color='c')
pyplot.title('model MAE/epoch 5/LSTM/batchSize 32/step 100')
pyplot.xlabel('epoch')
pyplot.ylabel('Error %')
pyplot.xlim([0.00, 4.00])
pyplot.legend(loc='upper right')
pyplot.show() 

pyplot.plot(history1.history['loss'],  label="loss", color="r")
pyplot.title('model MAE/epoch 5/BiLSTM/batchSize 32/step 100')
pyplot.xlabel('epoch')
pyplot.ylabel('Error %')
pyplot.xlim([0.00, 4.00])

pyplot.legend(loc='upper right')
pyplot.show()

pyplot.plot(history.history['loss'],  label="LSTM", color="c")
pyplot.plot(history1.history['loss'],  label="BiLSTM", color='r')
pyplot.title('Bi-LSTM vs LSTM')
pyplot.xlabel('epoch')
pyplot.ylabel('Error %')
pyplot.legend()
pyplot.show()