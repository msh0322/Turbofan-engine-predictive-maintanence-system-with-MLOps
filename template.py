"""
template.py

Scaffolds the project structure for:
    Turbofan-engine-predictive-maintanence-system-with-MLOps

Run once from the project root:
    python template.py

Safe to re-run: existing files are never overwritten.
"""

import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

PROJECT_NAME = "turbofan_pdm"  # Python package name (importable, no hyphens)

LIST_OF_FILES = [
    # ---- GitHub / CI-CD ----
    ".github/workflows/.gitkeep",
    ".github/workflows/ci.yaml",

    # ---- Package: top level ----
    f"src/{PROJECT_NAME}/__init__.py",

    # ---- Components (one per pipeline stage) ----
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/components/data_ingestion.py",
    f"src/{PROJECT_NAME}/components/data_validation.py",
    f"src/{PROJECT_NAME}/components/data_transformation.py",
    f"src/{PROJECT_NAME}/components/feature_engineering.py",
    f"src/{PROJECT_NAME}/components/model_trainer.py",
    f"src/{PROJECT_NAME}/components/model_evaluation.py",
    f"src/{PROJECT_NAME}/components/model_registry.py",

    # ---- Utilities ----
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",

    # ---- Config ----
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",

    # ---- Pipelines ----
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"src/{PROJECT_NAME}/pipeline/prediction_pipeline.py",

    # ---- Entities / constants / logging / exceptions ----
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/logger.py",
    f"src/{PROJECT_NAME}/exception.py",

    # ---- Config files ----
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    # ---- Data (kept out of git; folders tracked with .gitkeep) ----
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",

    # ---- Artifacts / models ----
    "artifacts/.gitkeep",
    "models/.gitkeep",

    # ---- Orchestration & MLOps ----
    "dvc.yaml",
    "main.py",
    "app.py",  # FastAPI / Flask serving app
    "monitoring/drift_detection.py",
    "monitoring/__init__.py",

    # ---- Notebooks ----
    "notebooks/01_eda.ipynb",
    "notebooks/02_modeling_experiments.ipynb",

    # ---- Tests ----
    "tests/__init__.py",
    "tests/test_data_ingestion.py",
    "tests/test_model.py",

    # ---- Web / API templates ----
    "templates/index.html",

    # ---- Docker & packaging ----
    "Dockerfile",
    ".dockerignore",
    "docker-compose.yaml",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    ".gitignore",
    "README.md",
]

# Optional starter content for selected files
DEFAULT_CONTENT = {
    "requirements.txt": (
        "pandas\nnumpy\nscikit-learn\nxgboost\ntensorflow\n"
        "mlflow\ndvc\nfastapi\nuvicorn\npyyaml\npython-box\n"
        "ensure\nevidently\npytest\n-e .\n"
    ),
    ".gitignore": (
        "__pycache__/\n*.pyc\n.venv/\nvenv/\n.env\n.ipynb_checkpoints/\n"
        "artifacts/*\n!artifacts/.gitkeep\n"
        "models/*\n!models/.gitkeep\n"
        "data/raw/*\n!data/raw/.gitkeep\n"
        "data/interim/*\n!data/interim/.gitkeep\n"
        "data/processed/*\n!data/processed/.gitkeep\n"
        "mlruns/\n*.egg-info/\n.DS_Store\n"
    ),
    "README.md": (
        "# Turbofan Engine Predictive Maintenance System with MLOps\n\n"
        "End-to-end Remaining Useful Life (RUL) prediction for turbofan engines "
        "(NASA C-MAPSS), with experiment tracking, data versioning, CI/CD, "
        "containerized serving, and drift monitoring.\n"
    ),
    "setup.py": (
        "from setuptools import find_packages, setup\n\n"
        "setup(\n"
        '    name="turbofan_pdm",\n'
        '    version="0.0.1",\n'
        '    author="your-name",\n'
        '    description="Turbofan engine predictive maintenance with MLOps",\n'
        '    package_dir={"": "src"},\n'
        '    packages=find_packages(where="src"),\n'
        ")\n"
    ),
    "Dockerfile": (
        "FROM python:3.10-slim\n"
        "WORKDIR /app\n"
        "COPY . /app\n"
        "RUN pip install --no-cache-dir -r requirements.txt\n"
        'CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]\n'
    ),
    f"src/{PROJECT_NAME}/logger.py": (
        "import logging\nimport os\nimport sys\n\n"
        'LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"\n'
        'LOG_DIR = "logs"\nLOG_FILE = os.path.join(LOG_DIR, "running_logs.log")\n'
        "os.makedirs(LOG_DIR, exist_ok=True)\n\n"
        "logging.basicConfig(\n"
        "    level=logging.INFO,\n"
        "    format=LOG_FORMAT,\n"
        "    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler(sys.stdout)],\n"
        ")\n\n"
        f'logger = logging.getLogger("{PROJECT_NAME}")\n'
    ),
}


def create_project_structure() -> None:
    for filepath_str in LIST_OF_FILES:
        filepath = Path(filepath_str)
        filedir = filepath.parent

        if str(filedir) != ".":
            filedir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Ensured directory: {filedir}")

        if not filepath.exists() or filepath.stat().st_size == 0:
            content = DEFAULT_CONTENT.get(filepath_str, "")
            filepath.write_text(content, encoding="utf-8")
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"Already exists, skipped: {filepath}")


if __name__ == "__main__":
    create_project_structure()