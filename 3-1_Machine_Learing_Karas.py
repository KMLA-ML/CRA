import pandas as pd

data = pd.read_excel("test_project.xlsx", index_col=0)

target = data["범죄율"]

del data["범죄율"]

data = data.values.tolist()

from sklearn.preprocessing import StandardScaler

X = data

scaler = StandardScaler()
scaler.fit(X)
scaled_data = scaler.transform(X)

import numpy as np

np_data = np.array(scaled_data)
np_target = np.array(target)

from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
from keras.optimizers import Adam


model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(51, )))
model.add(Dense(16, activation='relu'))

model.add(Dense(1))

model.compile(
    optimizer=Adam(lr=1e-3), 
    loss='mse'
)

hist = model.fit(
    np_data, np_target,
    epochs=500,
    validation_split=0.2
)
