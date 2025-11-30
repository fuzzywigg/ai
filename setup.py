from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fuzzywigg-ai",
    version="0.1.0",
    author="FuzzyWigg",
    description="Privacy-first, consent-based AI platform with blockchain integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fuzzywigg/fuzzywigg-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pre-commit",
        "black",
        "ruff",
        "python-dotenv",
        "stripe",
        "litellm",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
        ],
    },
)
