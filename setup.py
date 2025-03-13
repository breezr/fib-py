# use setup to define our parameters.
# use find_packages to exclude tests.
from setuptools import find_packages, setup

setup (
    name="andrew_fib_py",
    version="0.0.1",
    author="Andrew Pan",
    author_email="ycpan711@gmail.com",
    description="Calculate fibonacci numbers",
    long_description="A basic package for calculating fibonacci numbers.",
    long_description_content_type="text/markdown",
    url="https://github.com/breezr/fib-py",
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=["pytest"],
)
