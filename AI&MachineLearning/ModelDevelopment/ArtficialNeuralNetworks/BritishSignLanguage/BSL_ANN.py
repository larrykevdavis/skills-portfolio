# Generated from: BSL_ANN.ipynb
# Converted at: 2026-07-01T08:40:46.298Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

#Make sure to install the Keras, tensorflow and ann visualizer using the commands: 
#pip install tensorflow
#pip install keras

# # 1. Importing all the Required Libraries


#Importing the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import keras
from keras.models import Sequential 
from keras.layers import Dense, Dropout
from sklearn.metrics import accuracy_score 
import numpy as np

# # 2. Reading in the Dataset


dataset = pd.read_csv("BSL-leap-motion.csv")

# # 3. Exploratory Data Analysis


dataset.head()

# # 4. Data Cleaning


dataset=dataset.dropna(axis=0, how='any')

classes=list(dataset["CLASS"].unique())

for i in range(len(classes)):
    value=classes[i]
    floatvalue=float(i)
    dataset.loc[ dataset["CLASS"] == value,"CLASS"] = floatvalue


dataset

X = dataset.iloc[:,:-1] # Data

X = np.asarray(X).astype(np.float32)

y = dataset.iloc[:,-1] # Class labels

y= np.asarray(y).astype(np.float32)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# # 5. Model Creation


model = Sequential()
model.add(Dense(12, input_shape=(428,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.add(Dropout(rate = 0.1))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# # 6. Model Training


history=model.fit(X_train, y_train, batch_size = 10, epochs = 100)

# # 7. Model Prediction and Evaluation


best_model_accuracy = history.history['acc'][argmin(history.history['loss'])]