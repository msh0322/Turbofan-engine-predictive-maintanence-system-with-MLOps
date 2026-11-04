from setuptools import find_packages, setup

setup(
    name="turbofan_pdm",
    version="0.0.1",
    author="your-name",
    description="Turbofan engine predictive maintenance with MLOps",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
