# AI & Data Science Learning Repo

This repository contains coursework, notes, projects, and CI/CD integrations for notebooks, models, docs, and data versioning.

#  Data Science ML Learning Pipeline  
A complete end-to-end machine-learning project template including:
- ✅ Clean project structure (Cookiecutter-style)
- ✅ Experiment tracking & versioning
- ✅ CI/CD with GitHub Actions
- ✅ DVC for dataset + model artifacts
- ✅ MkDocs documentation site
- ✅ Docker environment
- ✅ Notebooks → HTML export
- ✅ Example ML pipeline with training + inference

This repository is designed to help you build skills while following best industry practices.

---

## Repository Structure

```bash
.
├── data/                       # DVC-managed datasets
│   ├── raw/                    # Unmodified data
│   ├── interim/                # Temporary transformed
│   └── processed/              # Training-ready
├── docs/                       # MkDocs documentation
│   └── index.md
├── models/                     # Trained model weights (DVC tracked)
├── notebooks/                  # Jupyter notebooks
│   ├── EDA.ipynb
│   └── model_dev.ipynb
├── src/                        # Source code (package)
│   ├── __init__.py
│   ├── data/                   # Data loading / preprocessing
│   │   ├── __init__.py
│   │   └── load.py
│   ├── features/               # Feature eng.
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/                 # Model code
│   │   ├── __init__.py
│   │   ├── train_model.py
│   │   └── predict_model.py
│   ├── pipelines/              # End-to-end pipeline
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── inference.py
│   └── visualization/          # Charts and figures
│       ├── __init__.py
│       └── visualize.py
├── tests/                      # Pytest unit tests
│   └── test_train.py
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # Lint + test + coverage
│   │   └── docs-deploy.yml     # MkDocs deployment
├── dvc.yaml                    # DVC pipeline definition
├── Dockerfile                  # Docker runtime
├── mkdocs.yml                  # Documentation config
├── requirements.txt
├── pyproject.toml              # Black, Ruff, etc.
├── .pre-commit-config.yaml
├── .gitignore
└── README.md

```
# Features
## ✅ ML Pipeline

Data loading → preprocessing

Feature engineering

Model training

Inference

Automatic artifact saving

## ✅ DVC (Data + Model Versioning)

Track:

Raw datasets

Preprocessed data

Model artifacts

```bash
dvc add data/raw
dvc push

```
## ✅ Notebooks → HTML Build

CI automatically converts notebooks:
```bash
notebooks/*.ipynb → artifacts/html/
```

## ✅ CI/CD

GitHub Actions

Linting (Ruff / Flake8)

Auto-formatting (Black)

Tests (pytest)

Coverage reporting

Notebook → HTML export

MkDocs → GitHub Pages deploy

## ✅ Pre-commit Hooks

Runs:

Ruff

Black

YAML/JSON checks

Enable:
```bash
pre-commit install
```
## ✅ Docker Support

Build:
```bash
docker build -t ai-ds .
```

Run:
```bash
docker run -it ai-ds
```

## ✅ Auto-Generated Docs

Uses MkDocs + mkdocs-material
```bash
mkdocs serve
```

## 🔧 Setup
Clone
```bash
git clone [<your-repo-url>](https://github.com/NSMovin/data_science_ml_learning_projects_roadmaps/edit/main/README.md)
cd repo
```

Install deps
```bash
pip install -r requirements.txt
```
Setup DVC
```bash
dvc init
dvc pull   # if remote exists
```
Pre-commit
```bash
pre-commit install
```
▶️ Run ML Pipeline
Train model
```bash
python -m src.pipelines.train
```
Inference
```bash
python -m src.pipelines.inference
```
✅ Testing
```bash
pytest -q
```

Coverage:
```bash
pytest --cov=src
```
📦 Model + Dataset Versioning (DVC)

Track:
```bash
dvc add data/raw
git add data/.gitignore data/raw.dvc
git commit -m "Add raw dataset"
```

Push:
```bash
dvc push
```
## 📄 Documentation

Build local docs:
```bash
mkdocs serve
```

Deployed automatically to GitHub Pages.

Access:
```
https://<username>.github.io/<repo>/
```
📓 Jupyter
```
jupyter notebook
```
