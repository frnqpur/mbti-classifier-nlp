# Security and Privacy Cleanup

## Goal
Before publishing this project to GitHub, Streamlit Community Cloud, Hugging Face Spaces, LinkedIn, or a portfolio website, remove files that may contain personal, sensitive, or unnecessary information.

## Do Not Publish Raw Personal Files
Avoid publishing files such as:

```text
Names.txt
Myquora.txt
Sanayapoem.txt
Valentin pyatev.txt
All text.txt
Their MBTI type.txt
```

These may contain personal names, writing samples, or identifiable information.

## Dataset Safety
Before uploading the dataset:

1. Check dataset license.
2. Do not expose raw personal text unnecessarily.
3. Avoid showing raw rows in the Streamlit app.
4. Use anonymous sample text for screenshots.
5. Do not include private notes or prompt history.

## Environment Files
Do not commit:

```text
.env
.env.local
secrets.toml
credentials.json
token.json
```

## Recommended .gitignore
Use this `.gitignore`:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/
env/

# Jupyter
.ipynb_checkpoints/

# Environment
.env
.env.local
secrets.toml
credentials.json
token.json

# Model artifacts
models/*.pkl
models/*.joblib

# Optional private data
private/
raw/
personal/
Names.txt
Myquora.txt
Sanayapoem.txt
Valentin pyatev.txt
All text.txt
Their MBTI type.txt

# System
.DS_Store
Thumbs.db
```

## Streamlit Secrets
If you use Streamlit secrets, keep them in:

```text
.streamlit/secrets.toml
```

Do not commit this file to public GitHub.

## Screenshot Safety
Before publishing screenshots, check that they do not show:

- names,
- emails,
- private text,
- raw dataset rows,
- file paths with personal usernames,
- API keys,
- credentials,
- private GitHub URLs.

## Public Demo Safety
The demo should:

- accept user input only,
- not display raw dataset rows,
- not expose training data,
- not show personal files,
- include educational disclaimer,
- avoid official psychological claims.

## Safe Disclaimer
Use this disclaimer in README and Streamlit app:

> This demo is for educational and portfolio purposes only. It is not an official psychological test and should not be used for diagnosis, hiring, counseling, or any sensitive decision-making.

## Final Pre-Publish Checklist
- [ ] README updated.
- [ ] Private files removed.
- [ ] `.env` not committed.
- [ ] Dataset license checked.
- [ ] Screenshot checked.
- [ ] Streamlit disclaimer visible.
- [ ] No official psychological claim.
- [ ] App runs locally.
- [ ] Deployment instructions included.
