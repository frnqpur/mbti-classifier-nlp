# Local Setup — MBTI Classifier

## Requirements
Recommended Python version:

```bash
Python 3.10 or 3.11
```

## Folder Structure
Recommended structure:

```text
05_mbti-classifier/
├── app.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
├── data/
│   └── Dataset.zip
├── models/
│   └── generated after training
├── screenshots/
└── portfolio-kit/
```

## Step 1 — Create Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3 — Prepare Dataset
Place the dataset file in one of these paths:

```text
Dataset.zip
```

or:

```text
data/Dataset.zip
```

The ZIP file should contain a CSV with at least these columns:

```text
type, posts
```

## Step 4 — Run Streamlit App

```bash
streamlit run app.py
```

## Step 5 — Open Local Demo
Streamlit usually opens the browser automatically. If not, open:

```text
http://localhost:8501
```

## Expected Local Behavior
The app should:

1. Load the MBTI dataset.
2. Train or load a simple Naive Bayes classifier.
3. Accept user text input.
4. Preprocess the text.
5. Predict MBTI-style traits.
6. Display confidence if available.
7. Show educational disclaimer.

## Common Issues

### Dataset Not Found
Make sure `Dataset.zip` is placed in the project root or inside `data/`.

### Missing Columns
The CSV inside the ZIP must contain:

```text
type
posts
```

### Slow Startup
The app may train models during first run. For deployment, it is better to cache training or pre-save model files if supported.

### NLTK Download Error
Use regex-based preprocessing in the Streamlit app to reduce dependency on online NLTK downloads during deployment.
