from setuptools import setup, find_packages

setup(
    name="kv_store",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=7.3.1",
        "pytest-cov>=4.1.0",
        "setuptools>=68.0.0",
    ],
)