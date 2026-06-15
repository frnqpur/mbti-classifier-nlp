# MBTI Classifier — NLP Text Classification Demo

## Overview
MBTI Classifier is an educational Natural Language Processing project that predicts MBTI-style personality traits from user-provided text. The project uses text preprocessing, bag-of-words style features, and Naive Bayes classifiers.

This project is designed as a machine learning portfolio demo and should not be treated as an official psychological assessment.

## Features
- Text input from user
- Text preprocessing
- MBTI-style trait prediction
- Naive Bayes classification
- Confidence display if available
- Streamlit web demo
- Educational disclaimer

## Tech Stack
- Python
- pandas
- NumPy
- NLTK
- Naive Bayes
- Streamlit

## Project Structure
```text
mbti-classifier-nlp/
├── app.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
├── mbti_classifier_notebook.ipynb
├── data/
│   └── dataset.zip
├── screenshots/
└── portfolio-kit/
```

## Dataset
The Dataset should contain at least two columns:

```text
type
posts
```

`type` contains MBTI labels, while `posts` contains text data.

For privacy reasons, raw personal text samples should not be displayed in the public demo.

## How It Works

### 1. Preprocessing
The text is cleaned by:

- converting to lowercase,
- removing URLs,
- removing punctuation and non-alphabetic characters,
- removing stopwords,
- extracting useful word tokens.

### 2. Feature Extraction
The cleaned text is represented using simple word-based features similar to bag-of-words.

### 3. Model
The demo uses Naive Bayes classifiers to predict MBTI-style traits:

- Introvert vs Extrovert
- Intuition vs Sensing
- Thinking vs Feeling
- Judging vs Perceiving

The predicted letters are combined into one MBTI-style output.

## Local Setup

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

## Deployment
Recommended deployment platforms:

1. Streamlit Community Cloud
2. Hugging Face Spaces

cPanel is not recommended because many shared hosting plans do not support Python ML dependencies such as pandas.

See:

```text
README_DEPLOY.md
STREAMLIT_DEPLOYMENT.md
```

## Disclaimer
This project is for educational and portfolio purposes only. The prediction result is not an official psychological assessment and must not be used for diagnosis, hiring, counseling, or other sensitive decisions.

## Limitations
- Baseline model only
- Simple feature extraction
- Dataset may contain bias
- Prediction depends on input text quality
- Not production-ready
- Not a psychological test

## Future Improvements
- Add TF-IDF feature extraction
- Try Logistic Regression or Linear SVM
- Add cross-validation
- Save trained model files
- Improve UI design
- Add model card
- Add more transparent evaluation metrics

## License
Use an appropriate license based on the dataset and project ownership.
