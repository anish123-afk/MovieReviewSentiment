import preprocessing
import os
import pickle
import tensorflow
from tensorflow import keras
from keras.layers import Embedding, LSTM, Dropout, Dense
from keras.models import Sequential

import matplotlib.pyplot as plt


X_train = preprocessing.X_train
y_train = preprocessing.y_train
X_test = preprocessing.X_test
y_test = preprocessing.y_test
X_val = preprocessing.X_val
y_val = preprocessing.y_val

tokenizer = preprocessing.tokenizer

model = Sequential()
model.add(Embedding(input_dim=15000, output_dim=128, input_length=400))
model.add(LSTM(64))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

# print(model.summary())


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=64)


os.makedirs("models", exist_ok=True)
os.makedirs("tokenizer", exist_ok=True)
model.save("models/sentiment_model_1.keras")
with open("tokenizer/tokenizer_1.pkl", "wb") as f:
    pickle.dump(tokenizer, f)


plt.figure()
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()
plt.savefig("models/accuracy_plot_1.png")
plt.show()

plt.figure()
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.savefig("models/loss_plot_1.png")
plt.show()