from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="foobar-fastapi-template-sqlite",
    version="0.1.1",
    author="Jarosław Maleszyk",
    author_email="j.maleszyk@gmail.com",
    description="A quick start template for FastAPI projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JarekMaleszyk/foobar-fastapi-template/",
    packages=find_packages(),
    include_package_data=True,
    # package_data={"fastapi_quickstart": ["alembic/*"]},
    install_requires=[
        "fastapi>=0.110.0",
        "uvicorn>=0.28.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "foobar-fastapi-template-sqlite=uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --reload",
        ],
    },
)