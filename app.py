"""
MBTI Classifier Demo - Streamlit

Educational demo based on the original MBTI text classification notebook.
It uses NLTK Naive Bayes classifiers with a simple bag-of-words pipeline.

Expected dataset location:
- Dataset.zip in the same folder as app.py, OR
- data/Dataset.zip, OR
- a CSV file inside data/ with columns: type, posts

Important:
This app is for portfolio/education only. It is not a psychological assessment tool.
"""

from __future__ import annotations

import os
import re
import string
import zipfile
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import nltk
import pandas as pd
import streamlit as st
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords

DATASET_CANDIDATES = [
    Path("data/dataset.zip"),
    Path("Dataset.zip"),
    Path("data/dataset.zip"),
]



APP_TITLE = "MBTI Text Classifier Demo"
RANDOM_STATE = 42
DEFAULT_MAX_FEATURES = 3500
DEFAULT_MAX_ROWS = 0  # 0 means use all rows. Set MBTI_MAX_ROWS env var to limit rows on small cloud instances.

TRAIT_CONFIG = [
    ("I", "E", "Introversion", "Extraversion"),
    ("N", "S", "Intuition", "Sensing"),
    ("T", "F", "Thinking", "Feeling"),
    ("J", "P", "Judging", "Perceiving"),
]


@st.cache_resource(show_spinner=False)
def get_stop_words() -> set[str]:
    """Load NLTK stopwords. Download only if missing."""
    try:
        return set(stopwords.words("english"))
    except LookupError:
        nltk.download("stopwords")
        return set(stopwords.words("english"))


def preprocess_text(text: str) -> List[str]:
    """Clean text and return tokens.

    This intentionally stays simple to match the original project style:
    lowercase, remove URL, punctuation, numbers, and English stopwords.
    """
    stop_words = get_stop_words()
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\|\|\|", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = [token for token in text.split() if token and token not in stop_words and len(token) > 1]
    return tokens


def find_dataset_file() -> Tuple[str, Path | None, str | None]:
    """Find Dataset.zip or CSV with MBTI dataset."""
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "Dataset.zip",
        base_dir / "data" / "Dataset.zip",
    ]

    for zip_path in candidates:
        if zip_path.exists():
            with zipfile.ZipFile(zip_path) as zf:
                csv_names = [name for name in zf.namelist() if name.lower().endswith(".csv")]
                if csv_names:
                    return "zip", zip_path, csv_names[0]

    data_dir = base_dir / "data"
    if data_dir.exists():
        csv_files = sorted(data_dir.glob("*.csv"))
        if csv_files:
            return "csv", csv_files[0], None

    return "missing", None, None


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    """Load dataset with columns `type` and `posts`."""
    source_type, path, csv_inside_zip = find_dataset_file()

    if source_type == "missing" or path is None:
        raise FileNotFoundError(
            "Dataset tidak ditemukan. Letakkan Dataset.zip di root project atau di folder data/."
        )

    if source_type == "zip":
        with zipfile.ZipFile(path) as zf:
            with zf.open(csv_inside_zip) as file_obj:
                df = pd.read_csv(file_obj)
    else:
        df = pd.read_csv(path)

    required_columns = {"type", "posts"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Dataset harus memiliki kolom: type dan posts.")

    df = df[["type", "posts"]].dropna().copy()
    df["type"] = df["type"].astype(str).str.upper().str.strip()
    df["posts"] = df["posts"].astype(str)
    df = df[df["type"].str.len() == 4]

    max_rows = int(os.getenv("MBTI_MAX_ROWS", DEFAULT_MAX_ROWS))
    if max_rows > 0 and len(df) > max_rows:
        df = df.sample(n=max_rows, random_state=RANDOM_STATE).reset_index(drop=True)

    return df.reset_index(drop=True)


def build_vocabulary(texts: Iterable[str], max_features: int = DEFAULT_MAX_FEATURES) -> set[str]:
    """Build vocabulary from the most common preprocessed tokens."""
    counter: Counter[str] = Counter()
    for text in texts:
        counter.update(preprocess_text(text))
    return {word for word, _ in counter.most_common(max_features)}


def extract_features(tokens: List[str], vocabulary: set[str]) -> Dict[str, bool]:
    """Sparse binary bag-of-words features for NLTK Naive Bayes."""
    token_set = set(tokens)
    return {f"contains({word})": True for word in token_set if word in vocabulary}


def make_trait_dataset(df: pd.DataFrame, left: str, right: str, vocabulary: set[str]):
    """Create labeled feature rows for one MBTI binary trait."""
    rows = []
    for mbti_type, posts in zip(df["type"], df["posts"]):
        if left in mbti_type:
            label = left
        elif right in mbti_type:
            label = right
        else:
            continue
        rows.append((extract_features(preprocess_text(posts), vocabulary), label))
    return rows


@st.cache_resource(show_spinner=True)
def train_trait_models(max_features: int = DEFAULT_MAX_FEATURES):
    """Train one Naive Bayes classifier per MBTI trait."""
    df = load_dataset()
    vocabulary = build_vocabulary(df["posts"], max_features=max_features)

    models = {}
    for left, right, left_name, right_name in TRAIT_CONFIG:
        training_rows = make_trait_dataset(df, left, right, vocabulary)
        classifier = NaiveBayesClassifier.train(training_rows)
        models[f"{left}{right}"] = {
            "classifier": classifier,
            "left": left,
            "right": right,
            "left_name": left_name,
            "right_name": right_name,
        }

    metadata = {
        "rows_used": len(df),
        "max_features": max_features,
        "vocabulary_size": len(vocabulary),
    }
    return models, vocabulary, metadata


def predict_mbti(text: str, models: dict, vocabulary: set[str]):
    """Predict MBTI type and confidence for each trait."""
    tokens = preprocess_text(text)
    features = extract_features(tokens, vocabulary)

    predicted_letters = []
    trait_results = []

    for key in ["IE", "NS", "TF", "JP"]:
        model_info = models[key]
        classifier = model_info["classifier"]
        prob_dist = classifier.prob_classify(features)
        predicted_label = prob_dist.max()
        confidence = float(prob_dist.prob(predicted_label))
        predicted_letters.append(predicted_label)

        trait_results.append(
            {
                "Trait": f"{model_info['left']} / {model_info['right']}",
                "Prediction": predicted_label,
                "Meaning": model_info["left_name"] if predicted_label == model_info["left"] else model_info["right_name"],
                "Confidence": confidence,
            }
        )

    return "".join(predicted_letters), trait_results, tokens


def render_disclaimer():
    st.warning(
        "Demo ini hanya untuk edukasi dan portfolio. Hasil prediksi bukan asesmen psikologis resmi, "
        "bukan diagnosis, dan tidak boleh digunakan untuk keputusan penting seperti hiring, seleksi, "
        "konseling, atau penilaian kepribadian formal."
    )


def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🧠", layout="centered")

    st.title("🧠 MBTI Text Classifier Demo")
    st.caption("Baseline NLP demo using text preprocessing + NLTK Naive Bayes classifiers")
    render_disclaimer()

    with st.sidebar:
        st.header("Model Info")
        st.write("Pipeline: regex preprocessing → bag-of-words → Naive Bayes")
        max_features = st.slider("Max vocabulary features", 1000, 6000, DEFAULT_MAX_FEATURES, step=500)
        st.caption("Naikkan fitur untuk eksperimen, turunkan jika deployment terasa berat.")

    try:
        with st.spinner("Loading dataset dan training model baseline..."):
            models, vocabulary, metadata = train_trait_models(max_features=max_features)

        with st.sidebar:
            st.success("Model ready")
            st.write(f"Rows used: {metadata['rows_used']:,}")
            st.write(f"Vocabulary size: {metadata['vocabulary_size']:,}")

    except Exception as exc:
        st.error("Aplikasi belum bisa dijalankan karena dataset/model belum tersedia.")
        st.code(str(exc))
        st.info(
            "Letakkan `Dataset.zip` di folder yang sama dengan `app.py`, atau buat folder `data/` "
            "lalu letakkan `Dataset.zip` / CSV dataset di dalamnya."
        )
        st.stop()

    sample_text = (
        "I enjoy exploring abstract ideas, writing reflections, and spending time thinking about future possibilities. "
        "I usually prefer meaningful conversations and structured plans."
    )

    user_text = st.text_area(
        "Masukkan teks untuk diprediksi",
        value=sample_text,
        height=180,
        help="Gunakan teks anonim. Jangan masukkan data pribadi/sensitif.",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        predict_clicked = st.button("Predict MBTI", type="primary")
    with col2:
        show_tokens = st.checkbox("Tampilkan token hasil preprocessing")

    if predict_clicked:
        if len(user_text.strip()) < 20:
            st.error("Masukkan teks yang lebih panjang agar prediksi lebih bermakna.")
            st.stop()

        predicted_type, trait_results, tokens = predict_mbti(user_text, models, vocabulary)

        st.subheader("Prediction Result")
        st.metric("Predicted MBTI Type", predicted_type)

        st.write("Confidence per trait:")
        result_df = pd.DataFrame(trait_results)
        result_df["Confidence"] = result_df["Confidence"].map(lambda value: f"{value:.2%}")
        st.dataframe(result_df, use_container_width=True, hide_index=True)

        if show_tokens:
            st.subheader("Preprocessed Tokens")
            st.write(tokens[:120])
            if len(tokens) > 120:
                st.caption(f"Menampilkan 120 token pertama dari total {len(tokens)} token.")

        st.info(
            "Interpretasi: confidence berasal dari distribusi probabilitas Naive Bayes untuk setiap trait, "
            "bukan ukuran validitas psikologis. Angka tinggi tidak berarti hasilnya benar secara psikologis."
        )

    st.divider()
    st.caption(
        "Built as an educational NLP baseline demo. Recommended portfolio wording: "
        "'baseline text classification experiment', not 'official personality predictor'."
    )


if __name__ == "__main__":
    main()