# -*- coding: utf8 -*-
from setuptools import setup, find_packages

requires = [
    'requests'
]

setup(
    name='ddns_client',
    version='0.0.1',
    maintainer='lipo',
    packages=find_packages(),
    install_requires=requires
)
