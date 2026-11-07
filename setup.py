from setuptools import find_packages,setup
from pathlib import Path
requirements=[line.strip()  for line in Path("requirements.txt").read_text(encoding="utf-8-sig").splitlines()
              if line.strip() and not line.startswith("#")
              ]


setup(
name="MachineLearning_Project",
version="0.1",
author="Deepak",
author_email="deepakumar22011999@gmail.com",
packages=find_packages(),
install_requires=requirements
)
