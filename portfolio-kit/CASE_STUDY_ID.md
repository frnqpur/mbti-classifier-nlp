# Studi Kasus — MBTI Classifier

## Ringkasan
MBTI Classifier adalah project NLP dan machine learning edukatif untuk mengeksplorasi klasifikasi tipe MBTI berdasarkan teks. Project ini menggunakan Python, text preprocessing, fitur bag-of-words, dan Naive Bayes classifier sebagai model baseline.

Project ini dibuat sebagai demonstrasi proses data science dari awal sampai akhir, bukan sebagai alat psikologi resmi.

## Latar Belakang
Teks dapat mengandung pola bahasa, gaya komunikasi, dan preferensi kata tertentu. Dalam project ini, pola tersebut digunakan sebagai input untuk model klasifikasi sederhana yang mencoba memprediksi komponen MBTI.

Namun, prediksi kepribadian dari teks memiliki banyak keterbatasan. Karena itu, hasil model harus dibaca sebagai eksperimen pembelajaran, bukan penilaian psikologis.

## Tujuan Project
Tujuan project ini adalah:

1. Membersihkan data teks.
2. Melakukan preprocessing NLP sederhana.
3. Mengubah teks menjadi fitur yang dapat dipahami model.
4. Melatih baseline classifier.
5. Mengevaluasi performa model.
6. Membuat demo interaktif menggunakan Streamlit.

## Dataset
Dataset berisi label MBTI dan kumpulan teks postingan. Kolom utama yang digunakan:

```text
type
posts
```

Kolom `type` berisi label MBTI seperti INFP, INFJ, INTP, dan lainnya. Kolom `posts` berisi kumpulan teks yang digunakan sebagai input model.

Untuk menjaga privasi dan keamanan, demo portfolio tidak menampilkan data mentah secara detail.

## Metodologi

### 1. Text Preprocessing
Tahapan preprocessing meliputi:

- mengubah teks menjadi lowercase,
- menghapus URL,
- menghapus karakter non-alfabet,
- menghapus punctuation,
- menghapus stopwords,
- mengambil token kata yang relevan.

### 2. Feature Extraction
Teks yang sudah dibersihkan diubah menjadi representasi sederhana berbasis kata. Pendekatan ini mirip bag-of-words, yaitu model melihat kehadiran kata tertentu sebagai fitur.

### 3. Model
Model yang digunakan adalah Naive Bayes classifier. Pendekatan ini sesuai untuk baseline text classification karena sederhana, cepat, dan mudah dijelaskan.

Untuk demo, prediksi dapat dilakukan melalui empat classifier biner:

- Introvert vs Extrovert
- Intuition vs Sensing
- Thinking vs Feeling
- Judging vs Perceiving

Hasil empat komponen tersebut kemudian digabung menjadi satu prediksi MBTI-style.

## Hasil
Model dapat memberikan prediksi MBTI-style dari teks input pengguna. Jika model menyediakan confidence, demo menampilkan tingkat keyakinan per komponen trait.

Namun, confidence bukan berarti validitas psikologis. Confidence hanya menunjukkan seberapa yakin model terhadap pola data yang dipelajari.

## Streamlit Demo
Demo Streamlit dibuat agar recruiter dapat mencoba project tanpa membuka notebook. User dapat memasukkan teks, lalu sistem akan memproses teks dan menampilkan prediksi.

Fitur demo:

- input teks manual,
- preprocessing otomatis,
- prediksi MBTI-style,
- confidence jika tersedia,
- disclaimer edukasi.

## Keterbatasan
Project ini memiliki beberapa keterbatasan:

1. Model masih baseline.
2. Feature extraction masih sederhana.
3. Dataset dapat mengandung bias.
4. Hasil tidak boleh digunakan sebagai asesmen psikologis.
5. Performa model bergantung pada kualitas dan panjang teks input.
6. Model belum production-ready.

## Future Improvement
Pengembangan berikutnya yang dapat dilakukan:

- menggunakan TF-IDF,
- mencoba Logistic Regression atau Linear SVM,
- menggunakan cross-validation,
- menyimpan model dengan pickle/joblib,
- menambahkan evaluation report,
- memperbaiki UI Streamlit,
- menambahkan contoh input anonim,
- menambahkan model card.

## Kesimpulan
Project ini menunjukkan kemampuan dasar dalam NLP, machine learning classification, dan deployment demo sederhana. Nilai utama project ini adalah proses pembelajaran, dokumentasi, dan kemampuan menjelaskan keterbatasan model secara bertanggung jawab.
