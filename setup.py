from setuptools import setup, find_packages

setup(
    name="farsnet",
    version="1.0",
    packages=find_packages(),
    package_data={"farsnet": ["database/farsnet2.5.db3"]},
    include_package_data=True,
    author="Arash Behmand",
    author_email="arashbehmand@gmail.com",
    description="Python implementation of FarsNet",
    license="MIT",
)
