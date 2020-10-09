

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textsummarizer", 
    version="0.0.1",
    author="Amy Jiang",
    author_email="amyhjiang@gmail.com",
    description="Library to auto-summarize text files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajiang36/textsummarizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)