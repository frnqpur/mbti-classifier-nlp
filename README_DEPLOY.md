# MBTI Classifier Streamlit Demo - Deployment Guide

## Ringkasan

Demo ini adalah aplikasi Streamlit sederhana untuk project **MBTI Text Classifier**. Aplikasi menerima input teks, melakukan preprocessing NLP sederhana, memprediksi 4 huruf MBTI menggunakan 4 classifier Naive Bayes, lalu menampilkan confidence per trait jika tersedia.

> Disclaimer: demo ini hanya untuk edukasi dan portfolio. Hasil prediksi bukan asesmen psikologis resmi, bukan diagnosis, dan tidak boleh digunakan untuk keputusan penting seperti hiring, seleksi, konseling, atau penilaian kepribadian formal.

## File yang dibutuhkan

Pastikan minimal ada file berikut di root repository:

```text
app.py
requirements.txt
README_DEPLOY.md
dataset.zip
```

Alternatif lokasi dataset:

```text
data/dataset.zip
```

Aplikasi juga bisa membaca CSV di folder `data/`, selama CSV memiliki kolom:

```text
type, posts
```

## Struktur folder yang disarankan

```text
mbti-classifier-demo/
├── app.py
├── requirements.txt
├── README_DEPLOY.md
├── dataset.zip
└── screenshots/
```

Jika ingin lebih rapi:

```text
mbti-classifier-demo/
├── app.py
├── requirements.txt
├── README_DEPLOY.md
├── data/
│   └── dataset.zip
└── screenshots/
```

## Local setup

### 1. Buat virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependency

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

Jika berhasil, browser akan membuka alamat lokal seperti:

```text
http://localhost:8501
```

## Catatan dataset

Aplikasi akan mencari dataset secara otomatis dari urutan berikut:

1. `dataset.zip` di root project.
2. `data/dataset.zip`.
3. File `.csv` pertama di folder `data/`.

Dataset harus memiliki kolom:

```text
type
posts
```

`type` berisi label MBTI seperti `INFP`, `INFJ`, `INTP`, dan seterusnya. `posts` berisi teks postingan.

## Cara kerja aplikasi

Pipeline aplikasi:

```text
User input text
↓
Lowercase + remove URL + remove punctuation + remove stopwords
↓
Binary bag-of-words features
↓
4 Naive Bayes classifiers:
- I vs E
- N vs S
- T vs F
- J vs P
↓
Predicted MBTI + confidence per trait
```

Confidence berasal dari distribusi probabilitas Naive Bayes. Confidence ini **bukan** ukuran validitas psikologis.

## Deploy ke Streamlit Community Cloud

### 1. Siapkan GitHub repository

Upload file berikut ke GitHub:

```text
app.py
requirements.txt
README_DEPLOY.md
dataset.zip
```

Atau gunakan:

```text
data/dataset.zip
```

Jangan upload file personal seperti:

```text
Names.txt
Myquora.txt
Sanayapoem.txt
Valentin pyatev.txt
All text.txt
Their MBTI type.txt
```

### 2. Buka Streamlit Community Cloud

1. Login ke Streamlit Community Cloud.
2. Pilih **New app**.
3. Pilih repository GitHub project.
4. Pilih branch, biasanya `main`.
5. Isi main file path:

```text
app.py
```

6. Klik **Deploy**.

Streamlit Community Cloud akan membaca `requirements.txt` untuk menginstall dependency Python.

### 3. Jika aplikasi lambat

Tambahkan environment variable berikut di pengaturan app:

```text
MBTI_MAX_ROWS=3000
```

Ini akan membatasi jumlah row dataset yang dipakai saat training di cloud. Untuk demo portfolio, ini boleh digunakan agar aplikasi lebih cepat.

## Deploy ke Hugging Face Spaces

### 1. Buat Space baru

1. Login ke Hugging Face.
2. Klik **New Space**.
3. Isi nama Space, misalnya:

```text
mbti-classifier-demo
```

4. Pilih SDK:

```text
Streamlit
```

5. Pilih visibility public atau private.
6. Klik **Create Space**.

### 2. Upload file

Upload file berikut:

```text
app.py
requirements.txt
README_DEPLOY.md
dataset.zip
```

Atau gunakan folder:

```text
data/dataset.zip
```

### 3. Pastikan metadata README Space benar

Untuk Hugging Face Spaces, README utama biasanya memiliki metadata YAML. Jika memakai README.md, contoh minimal:

```yaml
---
title: MBTI Classifier Demo
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
---
```

Jika kamu hanya memakai `README_DEPLOY.md`, pastikan di pengaturan Space tetap memilih SDK Streamlit dan app file `app.py`.

## Rekomendasi untuk portfolio recruiter

Gunakan wording aman seperti:

```text
Built an educational NLP baseline demo that predicts MBTI traits from text using preprocessing, bag-of-words features, and Naive Bayes classifiers. The project includes transparent limitations and a disclaimer that predictions are not official psychological assessments.
```

Jangan gunakan wording seperti:

```text
Built an accurate psychological personality predictor.
```

## Acceptance criteria

Aplikasi siap demo jika:

- [ ] `streamlit run app.py` berhasil di lokal.
- [ ] User bisa input teks.
- [ ] Aplikasi menampilkan prediksi MBTI.
- [ ] Aplikasi menampilkan confidence per trait.
- [ ] Aplikasi menampilkan disclaimer edukasi.
- [ ] Tidak ada file personal yang dipublish.
- [ ] `requirements.txt` berada di root repository.
- [ ] Dataset berada di `dataset.zip` root atau `data/dataset.zip`.
- [ ] Demo tidak mengklaim hasil sebagai asesmen psikologis resmi.

## Troubleshooting

### Error: Dataset tidak ditemukan

Pastikan ada salah satu file berikut:

```text
dataset.zip
data/dataset.zip
data/nama_dataset.csv
```

### Error: Dataset harus memiliki kolom type dan posts

Pastikan CSV memiliki kolom:

```text
type, posts
```

### Aplikasi terlalu lambat saat deploy

Gunakan environment variable:

```text
MBTI_MAX_ROWS=3000
```

Atau turunkan slider `Max vocabulary features` di sidebar.

### NLTK stopwords error

Aplikasi sudah mencoba download stopwords otomatis. Jika masih error, jalankan lokal:

```python
import nltk
nltk.download("stopwords")
```
