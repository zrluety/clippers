from setuptools import setup, find_packages

install_requires = [
    "colorama",
]

tests_require = [
    "pytest",
    "pytest-cov",
]

setup(
    name="clippers",
    version="0.1",
    author="Zachary Luety",
    author_email="zluety@gpwa.com",
    packages=find_packages(exclude=["tests"]),
    description="Build beautiful Command Line Applications in Python",
    install_requires=install_requires,
    tests_require=tests_require
)