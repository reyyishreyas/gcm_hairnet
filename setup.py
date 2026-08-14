from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gcm-hairnet",
    version="0.1.0",
    description="Research-grade repository for GCM-HAIRNet",
    author="GCM-HAIRNet Authors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*", "scripts*", "configs*", "docs*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
        "tensorboard>=2.14.0",
        "matplotlib>=3.7.0",
        "pillow>=10.0.0",
        "scikit-learn>=1.3.0",
        "einops>=0.7.0",
        "timm>=0.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
        ],
    },
)
