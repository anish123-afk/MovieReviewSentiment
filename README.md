<div align="center">

# 🎬 Movie Review Sentiment Analyzer

**An LSTM-powered deep learning model that reads a movie review and tells you if it's positive or negative — with a sleek desktop GUI to match.**

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## What is this?

This project trains an LSTM neural network on 50,000 IMDB movie reviews to classify sentiment as **Positive** or **Negative**, then wraps the trained model in a clean, dark-themed Tkinter desktop app — type in a review, hit analyze, and get an instant prediction with a confidence score.

It covers the full pipeline: raw text → cleaning → tokenization → padding → LSTM model → evaluation → a usable GUI on top.

---

## Features

- 🧠 **LSTM-based classifier** trained on a perfectly balanced 50k-review dataset (25k positive / 25k negative)
- 🧹 **Text preprocessing pipeline** — HTML/URL stripping
- 🔤 **Custom tokenizer** (15,000-word vocabulary with out-of-vocabulary handling), saved alongside the model for consistent predictions
- 📊 **Full evaluation suite** — accuracy, precision, recall, F1, and confusion matrix
- 🖥️ **Dark-mode desktop GUI** built with Tkinter — paste a review, get a Positive/Negative badge with confidence %
- 💾 **Reusable saved model + tokenizer** so you can predict on new text without retraining

---

## Project Structure

```
MovieReviewSentiment/
│
├── dataset/
│   └── imdb.csv              # 50,000 labeled movie reviews
│
├── models/
│   └── sentiment_model.keras # Trained LSTM model
│
├── tokenizer/
│   └── tokenizer.pkl         # Fitted tokenizer (word → integer mapping)
│
├── EDA.py                    # Exploratory data analysis — class balance, review length stats & plots
├── preprocessing.py          # Cleans, tokenizes, pads, and splits the data (train/val/test)
├── train.py                  # Training loop, saves accuracy/loss curves (train vs. val), saves model
├── evaluation.py             # Accuracy, precision, recall, F1, confusion matrix on the test set
├── prediction.py             # Loads saved model/tokenizer, exposes predict_sentiment()
├── gui.py                    # Tkinter desktop app for interactive predictions
└── README.md
```

---

## How it works

1. **Explore (`EDA.py`)** — checks class balance (25k positive / 25k negative) and review length distribution to inform preprocessing choices like max sequence length
2. **Preprocess (`preprocessing.py`)**
   - **Clean** — strip HTML tags/URLs
   - **Tokenize** — build a 15,000-word vocabulary, map each word to an integer, with an `<OOV>` token for unseen words
   - **Pad** — every review is padded/truncated to a fixed length (`MAX_SEQUENCE_LENGTH = 400`) so the LSTM can process it
   - **Split** — 70% train / 10% validation / 20% test, stratified to preserve the 50/50 class balance
3. **Model architecture** (built in `train.py`):

   | Layer | Purpose |
   |---|---|
   | `Embedding(15000, 128)` | Turns each word-integer into a learned 128-dim vector |
   | `LSTM(64)` | Reads the sequence, learns context, order, and negation |
   | `Dropout(0.5)` | Randomly disables 50% of neurons per step to reduce overfitting |
   | `Dense(1, sigmoid)` | Squashes output to a single 0–1 positive-sentiment probability |

4. **Train (`train.py`)** — Adam optimizer, binary crossentropy loss, tracked via accuracy on train/validation sets; plots accuracy and loss curves (train vs. val) per epoch and saves the trained model + tokenizer
5. **Evaluate (`evaluation.py`)** — accuracy, precision, recall, F1 score, and a confusion matrix on the held-out test set
6. **Serve (`prediction.py` / `gui.py`)** — the saved model and tokenizer are loaded for one-off predictions or the interactive GUI

---

## Getting Started

### 1. Prerequisites

- Python 3.8 or higher
- pip

### 2. Clone the repository

```bash
git clone https://github.com/anish123-afk/MovieReviewSentiment.git
cd MovieReviewSentiment
```

### 3. Install dependencies

```bash
pip install pandas numpy tensorflow scikit-learn matplotlib
```

### 4. Add the dataset

Place your IMDB reviews CSV at `dataset/imdb.csv` with two columns: `review` and `sentiment`.

### 5. Explore the data (optional)

```bash
python EDA.py
```

Shows class balance and review length distribution — useful context before training.

### 6. Preprocess the data

```bash
python preprocessing.py
```

Cleans, tokenizes, pads, and splits the dataset into train/val/test sets.

### 7. Train the model

```bash
python train.py
```

Trains for 100 epochs, plots training vs. validation accuracy/loss curves, and saves `models/sentiment_model.keras` and `tokenizer/tokenizer.pkl`.

### 8. Evaluate the model

```bash
python evaluation.py
```

Prints accuracy, precision, recall, F1 score, and the confusion matrix on the test set.

### 9. Run predictions from the command line

```bash
python prediction.py
```

### 10. Launch the GUI

```bash
python gui.py
```

Type a review into the text box, click **🔍 Analyze Sentiment**, and see the Positive/Negative badge with a confidence percentage.


---

## Model Performance

_Fill in with your actual test-set numbers after training:_

| Metric | Score |
|---|---|
| Accuracy | `87.79%` |
| Precision | `87.72%` |
| Recall | `87.88%` |
| F1 Score | `87.80%` |

---

## Dependencies

| Package | Purpose |
|---|---|
| `pandas` | Loading and exploring the dataset |
| `numpy` | Numerical operations |
| `tensorflow` / `keras` | Building, training, and running the LSTM model |
| `scikit-learn` | Train/val/test splitting and evaluation metrics |
| `matplotlib` | Data exploration plots |
| `tkinter` | Desktop GUI (built into Python) |

---
