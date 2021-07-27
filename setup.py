from setuptools import find_packages, setup
import re

PACKAGE_NAME = "image-comparer"
PACKAGE_NAME_UNDERLINE = PACKAGE_NAME.replace("-", "_")

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open(f'{PACKAGE_NAME_UNDERLINE}/__init__.py').read(),
    re.M
    ).group(1)

setup(
    name=PACKAGE_NAME,
    packages=find_packages(exclude=["tests"]),
    version=version,
    description='Compares two images using siamese networks',
    long_description=open("README.rst", "r").read(),
    long_description_content_type='text/x-rst',
    author='joeyism',
    url='https://github.com/joeyism/py-image-comparer',
    download_url='https://github.com/joeyism/py-image-comparer/archive/{}.tar.gz'.format(version),
    install_requires=[package for package in open("requirements.txt").read().split("\n")],
    keywords=["pytorch", "torch", "machine", "learning", "image", "compare", "comparer", "siamese", "network", "networks"],
    entry_points={
        "console_scripts": [
            f"image-compare = {PACKAGE_NAME_UNDERLINE}.cli:cli",
        ]
    },
    package_data={"": ["*.txt", "*.cfg"]},
    include_package_data=True,
)
