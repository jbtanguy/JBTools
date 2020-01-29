from setuptools import setup, find_packages

from JBTools import __version__

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="JBTools",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    description="My personal packages",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=[
        ""
    ],
    url="https://github.com/jbtanguy/JBTools.git",
    author='Jean-Baptiste Tanguy',
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)
