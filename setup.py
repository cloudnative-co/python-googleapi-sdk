from setuptools import setup, find_packages

setup(
    name="GoogleAPI",
    version="0.2.0",
    description="GoogleAPI for Python 3.6",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
