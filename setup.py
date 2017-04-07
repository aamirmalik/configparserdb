#!/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='configparserdb',
    version='0.1.0',
    description='Python package to access config parser based database',
    long_description=readme,
    author='Aamir Malik',
    author_email='aamirm@gmail.com',
    url='https://github.com/aamirmalik/configparserdb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

