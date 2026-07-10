import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/IMDB Dataset.csv')

list_length = []

def check_length(sentence):
    list_of_words = sentence.split(" ")

    return len(list_of_words)

def calc_avg(list_length):
    total = 0

    for length in list_length:
        total += length

    return total / len(df)

# print the dataset 
def print_head():
    return df.head()

# check the null values
def check_null():
    return df.isnull().sum()

def columns_name():
    return df.columns

# distribution of sentiments
def distribution_sentiment():
    return df['sentiment'].value_counts()


# print(df['review'][0])


for i in range(len(df)):
    length = check_length(df['review'][i])
    list_length.append(length)

def lengh_analysis():
    print(f"The max len is : {max(list_length)}")
    print(f"The max len is : {min(list_length)}")
    print(f"The max len is : {calc_avg(list_length)}")

def graph_wordDistribution():
    plt.figure(figsize=(12, 6))
    plt.hist(list_length, bins = 50)
    plt.xlabel("Number of Words")
    plt.ylabel("Number of Reviews")
    plt.show()

