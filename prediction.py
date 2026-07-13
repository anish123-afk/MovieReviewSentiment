
import pickle
import tensorflow
from tensorflow import keras
from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences

model = load_model("models/sentiment_model_1.keras")
with open("tokenizer/tokenizer_1.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=400, padding="post")
    prob = model.predict(padded)[0][0]
    if prob >= 0.5:
        label = "positive"
        confidence = prob
    else:
        label = "negative"
        confidence = 1 - prob
    return label, f"{confidence*100:.1f}%"

# if __name__ == "__main__":
