from setuptools import setup, find_packages

setup(
    name="farsnet",
    version="1.0",
    packages=find_packages(),
    package_data = {
    'farsnet' : ['farsnet2.5.db3'],
    },
    include_package_data = True
)

