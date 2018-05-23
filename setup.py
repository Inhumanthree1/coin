import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coin",
    version="0.0.1",
    author="Robert Fox",
    author_email="inhumanthree1@protonmail.com",
    description="A package I made to learn pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inhumanthree1/coin",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
