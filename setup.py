#!/usr/bin/env python
from setuptools import setup

exec(open("gocoin/version.py").read())

setup(
    name='gocoin-python',
    version=__version__,
    description='This client library is designed to support the GoCoin API'
    author='GoCoin',
    maintainer='Kevin Beauregard',
    maintainer_email='kevin@gocoin.com',
    url='https://github.com/GoCoin/gocoin-python',
    license='Apache 2.0',
    packages=["gocoin"],
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires=[
        'requests',
    ],
)
