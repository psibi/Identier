#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__author__ = 'Sibi <sibi@psibi.in>'
__version__ = '0.1.2'  #major.minor.micro

setup(
    # Basic package information.
    name='identi',
    version=__version__,
    packages=find_packages(),

    # Packaging options.
    include_package_data=True,

    # Package dependencies.
    install_requires=['oauth2', 'requests', 'requests-oauth','django'],

    # Metadata for PyPI.
    author='Sibi',
    author_email='sibi@psibi.in',
    license='GNU GPLv3',
    url='https://github.com/psibi/Identier',
    keywords='identi.ca API library',
    description='An easy to use API library specifically for identi.ca',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet'
    ]
)
