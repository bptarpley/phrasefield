#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='phrasefield',
    version='0.1',
    description='PhraseField',
    author='Bryan Tarpley',
    author_email='bptarpley@gmail.com',
    license='GNU General Public License',
    install_requires=['django', 'mmh3', 'nltk'],
    packages=find_packages(),
    package_data={'phrasefield.web.static' : ['*'],},
    include_package_data=True,
    zip_safe=False,
)
