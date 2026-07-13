import EDA
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# cleaning 
df = EDA.df

def clean_review(review):
    final_review = ""
    inside = False

    for ch in review:
        if ch == "<":
            inside = True
        elif ch == ">":
            inside = False
        elif inside == False:
            final_review += ch

    return final_review

def cleaning_dataset():
    df['clean'] = ''
    for i in range(len(df)):
        review = df['review'][i]
        final_review = clean_review(review)
        df['clean'][i] = final_review
    return df

df = cleaning_dataset()


tokenizer = Tokenizer(num_words=15000, oov_token="OOV")
tokenizer.fit_on_texts(df['clean'])

sequences = tokenizer.texts_to_sequences(df['clean'])   

X = pad_sequences(sequences, padding="post", maxlen=400)
y = np.where(df['sentiment'].values == 'positive', 1, 0)

def train_test_val_split(X, y):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=1/3, random_state=42, stratify=y_temp)

    return X_train, y_train, X_test, y_test, X_val, y_val

X_train, y_train, X_test, y_test, X_val, y_val = train_test_val_split(X, y)