import sys
from setuptools import setup, find_packages

setup(
    name='result',
    description='',
    long_description='',
    url='https://github.com/EntilZha/result',
    author='Pedro Rodriguez',
    author_email='ski.rodriguez@gmail.com',
    maintainer='Pedro Rodriguez',
    maintainer_email='ski.rodriguez@gmail.com',
    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'test']),
    version='0.0.0',
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
