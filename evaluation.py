from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import preprocessing
# import train
import tensorflow
from tensorflow import keras
from keras.models import load_model

import matplotlib.pyplot as plt

X_test = preprocessing.X_test
y_test = preprocessing.y_test

# history = train.history

model = load_model("models/sentiment_model_1.keras")

y_prob = model.predict(X_test)
y_pred = (y_prob >= 0.5).astype(int)

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


