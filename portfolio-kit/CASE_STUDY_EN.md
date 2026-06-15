# Case Study — MBTI Classifier

## Overview
MBTI Classifier is an educational NLP and machine learning project that explores MBTI-style text classification. The project uses Python, text preprocessing, bag-of-words style features, and a Naive Bayes classifier as a baseline model.

This project is designed as an end-to-end data science portfolio project, not as an official psychological assessment tool.

## Background
Written text may contain patterns in word choice, communication style, and expression. This project explores whether those patterns can be used by a simple classifier to predict MBTI-style personality traits.

However, personality prediction from text has many limitations. Therefore, the model output should be interpreted as an educational machine learning experiment, not as a psychological result.

## Project Goals
The goals of this project are to:

1. Clean text data.
2. Apply basic NLP preprocessing.
3. Convert text into model-readable features.
4. Train a baseline classifier.
5. Evaluate model performance.
6. Build a simple interactive Streamlit demo.

## Dataset
The dataset contains MBTI labels and text posts. The main columns are:

```text
type
posts
```

The `type` column contains MBTI labels such as INFP, INFJ, INTP, and others. The `posts` column contains text used as model input.

For privacy and safety, the public portfolio demo should not expose raw personal text samples.

## Methodology

### 1. Text Preprocessing
The preprocessing steps include:

- converting text to lowercase,
- removing URLs,
- removing non-alphabetic characters,
- removing punctuation,
- removing stopwords,
- extracting relevant word tokens.

### 2. Feature Extraction
The cleaned text is converted into a simple word-based representation. This approach is similar to bag-of-words, where the model uses word presence as input features.

### 3. Model
The model used is a Naive Bayes classifier. This is suitable as a baseline for text classification because it is simple, fast, and easy to explain.

For the demo, prediction can be handled through four binary classifiers:

- Introvert vs Extrovert
- Intuition vs Sensing
- Thinking vs Feeling
- Judging vs Perceiving

The four predicted components are combined into one MBTI-style output.

## Result
The model can generate an MBTI-style prediction from user input text. If confidence values are available, the demo displays trait-level confidence.

However, model confidence does not mean psychological validity. It only reflects how strongly the model associates the input text with patterns learned from the training data.

## Streamlit Demo
The Streamlit demo allows recruiters or visitors to try the project without opening the notebook. Users can enter text, run prediction, and view the output interactively.

Demo features:

- manual text input,
- automatic preprocessing,
- MBTI-style prediction,
- confidence values if available,
- educational disclaimer.

## Limitations
This project has several limitations:

1. The model is a baseline model.
2. Feature extraction is simple.
3. The dataset may contain bias.
4. The result must not be used as a psychological assessment.
5. Prediction quality depends on input length and quality.
6. The system is not production-ready.

## Future Improvements
Possible improvements include:

- using TF-IDF features,
- trying Logistic Regression or Linear SVM,
- adding cross-validation,
- saving models with pickle or joblib,
- adding detailed evaluation reports,
- improving the Streamlit UI,
- adding anonymous sample inputs,
- creating a model card.

## Conclusion
This project demonstrates fundamental skills in NLP, machine learning classification, and simple deployment. Its main value is the workflow, documentation, and responsible communication of model limitations.
