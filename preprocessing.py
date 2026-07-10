import EDA
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.text import Tokenizer

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
print(df['clean'][0])
print(df['review'][0])


def tokenizing():
    df['np_sequences'] = None
    
    tokenizer = Tokenizer(num_words= 150000, oov_token="OOV")
    tokenizer.fit_on_texts(df['clean'])
    for i in range(len(df)):
        review = df['clean'][i]
        sequences = tokenizer.texts_to_sequences([review])
        df.at[i, 'np_sequences'] = np.array(sequences)
    return df

df = tokenizing()
print(df['clean'][0])
print(df['review'][0])
print(df['np_sequences'][0])
