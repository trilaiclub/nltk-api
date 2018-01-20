
from setuptools import setup, find_packages
import sys, os

setup(name='reco',
    version='0.0.1',
    description="Testing",
    long_description="Testing",
    classifiers=[],
    keywords='',
    author='TRIL AI Club',
    author_email='trilaiclub@gmail.com',
    url='trilaiclub.org',
    license='Open Source',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        reco = reco.cli.main:main
    """,
    namespace_packages=[],
    )
