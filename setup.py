from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="advanced-logger",
    version="1.0.0.1",
    author="WNS",
    author_email="wnsoff@yandex.ru",
    description="Advanced logging utility with file and stream handlers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wns444/LoggerModule.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8',
    keywords='logging, logger, utility',
)