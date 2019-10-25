from setuptools import setup

setup(
    name="test-case",
    version="0.1.0",
    author="Aleksandr Donskoi",
    author_email="donskoy.alexander@gmail.com",
    packages=["case"],
    entry_points={"console_scripts": ["test-case = case.__main__:main"]},
)
