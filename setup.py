#!/usr/bin/env python
from setuptools import setup


GITHUB_URL = 'https:github.com/jonas-hagen/bootstrap-sources'
VERSION = '4.0.0-1'

setup(
    author='Jonas Hagen',
    author_email='jonas.hagen3@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 3.6',
    ],
    description='Twitter boutstrap sources as pypi package.',
    download_url=('{url}/archive/v{version}.tar.gz'
                  .format(url=GITHUB_URL,
                          version=VERSION)),
    license='MIT',
    maintainer='Jonas Hagen',
    maintainer_email='jonas.hagen3@gmail.com',
    name='bootstrap-sources',
    packages=['bootstrap_sources'],
    package_data={
        'bootstrap_sources': ['js/*.js', 'scss/*.scss', 'scss/*/*.scss'],
    },
    python_requires='>=3.5.*, <4',
    version=VERSION,
)
