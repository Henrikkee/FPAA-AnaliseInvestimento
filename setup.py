from setuptools import setup, find_packages

setup(
    name="paa-project",
    version="0.0.1",
    author="Henrique Monteiro",
    description="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["paa-project = src.main:main"]},
)