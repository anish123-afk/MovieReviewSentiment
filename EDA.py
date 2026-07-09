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
print(df.head())

# check the null values
print(df.isnull().sum())

print(df.columns)

# distribution of sentiments
print(df['sentiment'].value_counts())

# shape
print(df.shape)

# print(df['review'][0])


for i in range(len(df)):
    length = check_length(df['review'][i])
    list_length.append(length)

print(f"The max len is : {max(list_length)}")
print(f"The max len is : {min(list_length)}")
print(f"The max len is : {calc_avg(list_length)}")

plt.figure(figsize=(12, 6))
plt.hist(list_length, bins = 50)
plt.xlabel("Number of Words")
plt.ylabel("Number of Reviews")
# plt.show()