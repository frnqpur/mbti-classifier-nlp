# Streamlit Deployment Guide

## Recommended Deployment Targets
Because standard cPanel hosting often does not support Python ML dependencies such as pandas, this project should be deployed using:

1. Streamlit Community Cloud
2. Hugging Face Spaces

Do not prioritize cPanel for this project.

---

# Option A — Deploy to Streamlit Community Cloud

## Files Needed
Your GitHub repository should contain:

```text
app.py
requirements.txt
README.md
README_DEPLOY.md
Dataset.zip
```

or:

```text
app.py
requirements.txt
README.md
README_DEPLOY.md
data/Dataset.zip
```

## Steps

1. Create or open a GitHub repository.
2. Upload the project files.
3. Go to Streamlit Community Cloud.
4. Click **New app**.
5. Select your GitHub repository.
6. Select branch, usually `main`.
7. Set main file path:

```text
app.py
```

8. Click **Deploy**.

## Recommended Streamlit Settings
If the app is slow, reduce dataset size during training using an environment variable such as:

```text
MBTI_MAX_ROWS=3000
```

This keeps the demo lightweight and recruiter-friendly.

## Streamlit Notes
For recruiter demo, avoid showing raw dataset rows that may contain personal writing samples. The app should focus on user input, prediction output, confidence, and disclaimer.

---

# Option B — Deploy to Hugging Face Spaces

## Files Needed
For Hugging Face Spaces, include:

```text
app.py
requirements.txt
README.md
Dataset.zip
```

or:

```text
app.py
requirements.txt
README.md
data/Dataset.zip
```

## Create a New Space
1. Go to Hugging Face.
2. Create **New Space**.
3. Choose SDK:

```text
Streamlit
```

4. Upload project files.
5. Wait for the Space to build.

## Recommended README Metadata
For Hugging Face Spaces, the top of `README.md` can include:

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

## Hugging Face Notes
Hugging Face Spaces is suitable if you want a clean public demo link for your portfolio.

---

# Deployment Acceptance Criteria

The deployed demo is acceptable if:

- app opens without error,
- text input works,
- prediction appears after clicking the button,
- confidence appears if supported by the model,
- educational disclaimer is visible,
- no private text files are exposed,
- no official psychological claim is made,
- README explains limitations clearly.
