"""
This file is to combine all the packages available into a distribution bundle
"""
from setuptools import setup, find_packages

setup(
    name="bundle_by_indrajit",
    version="1.0.0",
    author="indrajit",
    author_email="indrajit411@gmail.com",
    description="Ready to use package distribution bundle by indrajit",
    packages=find_packages(include=["hello_world", "second_package"]),
)
