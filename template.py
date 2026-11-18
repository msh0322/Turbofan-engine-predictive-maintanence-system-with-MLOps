
from pathlib import Path

# Project name
project_name = "turbofan_predictive_maintenance"

# Main project directories
directories = [
    f"{project_name}/components",
    f"{project_name}/configuration",
    f"{project_name}/constants",
    f"{project_name}/entity",
    f"{project_name}/exception",
    f"{project_name}/logger",
    f"{project_name}/pipeline",
    f"{project_name}/utils",

    "data/raw",
    "data/processed",
    "data/external",

    "notebooks",
    "config",
    "monitoring",
    "tests",
    "api",
    "dashboard",
    "artifacts",
    "reports",
    "logs",
    "requirements",
]

# Project files
list_of_files = [

    # Package initialization
    f"{project_name}/__init__.py",

    # Components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/feature_engineering.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/data_drift.py",
    f"{project_name}/components/model_monitoring.py",

    # Configuration
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",

    # Constants
    f"{project_name}/constants/__init__.py",

    # Entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    # Exception handling
    f"{project_name}/exception/__init__.py",

    # Logging
    f"{project_name}/logger/__init__.py",

    # Training and prediction pipelines
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # Utilities
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # API
    "api/__init__.py",
    "api/main.py",

    # Dashboard
    "dashboard/app.py",

    # Monitoring
    "monitoring/monitoring_config.yaml",

    # Configuration files
    "config/model.yaml",
    "config/schema.yaml",

    # Requirements
    "requirements.txt",
    "requirements/base.txt",
    "requirements/training.txt",
    "requirements/api.txt",
    "requirements/dashboard.txt",
    "requirements/dev.txt",

    # Testing
    "tests/__init__.py",
    "tests/test_ingestion.py",
    "tests/test_transformation.py",
    "tests/test_prediction.py",

    # Notebooks
    "notebooks/README.md",

    # Project configuration
    "app.py",
    "demo.py",
    "setup.py",
    "Dockerfile",
    "docker-compose.yml",
    ".dockerignore",
    ".gitignore",
    ".env.example",
    "dvc.yaml",
    "params.yaml",
    "README.md",
]


def create_directories():
    """Create all project directories."""

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Directory created/verified: {directory}")


def create_files():
    """Create project files without overwriting existing content."""

    for filepath in list_of_files:

        path = Path(filepath)

        # Create parent directories
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create file only if it does not exist
        if not path.exists():
            path.touch()
            print(f"Created: {path}")

        else:
            print(f"Already exists: {path}")


if __name__ == "__main__":

    create_directories()
    create_files()

    print("\n" + "=" * 55)
    print("TURBOFAN PROJECT STRUCTURE CREATED SUCCESSFULLY!")
    print("=" * 55)
