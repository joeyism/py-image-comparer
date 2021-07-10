from setuptools import find_packages, setup

PACKAGE_NAME = "image-comparer"
PACKAGE_NAME_UNDERLINE = PACKAGE_NAME.replace("-", "_")

setup(
    name=PACKAGE_NAME,
    packages=find_packages(exclude=["tests"]),
    install_requires=[package for package in open("requirements.txt").read().split("\n")],
    entry_points={
        "console_scripts": [
            f"image-compare = {PACKAGE_NAME_UNDERLINE}.cli:cli",
        ]
    },
    package_data={"": ["*.txt", "*.cfg"]},
    include_package_data=True,
)
