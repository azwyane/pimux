import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pimux", 
    version="2.0.0",
    author="azwane",
    author_email="debianbyte@gmail.com",
    description="A package for accessing termux-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azwyane/pymux.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
