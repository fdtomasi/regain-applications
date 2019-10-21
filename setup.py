#!/usr/bin/python
"""regainapp setup script.

Author: Federico Tomasi
Copyright (c) 2017-2019, Federico Tomasi.
Licensed under the BSD 3-Clause License (see LICENSE.txt).
"""

from setuptools import setup, find_packages
# import numpy as np

# Package Version
from regainapp import __version__ as version
setup(
    name='regainapp',
    version=version,

    description=('regain-applications'),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Federico Tomasi',
    author_email='fdtomasi@gmail.com',
    maintainer='Federico Tomasi',
    maintainer_email='fdtomasi@gmail.com',
    url='https://github.com/fdtomasi/regain-applications',
    download_url='https://github.com/fdtomasi/regain-applications/archive/'
                 'v%s.tar.gz' % version,
    keywords=['graph inference', 'latent variables'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python'
    ],
    license='FreeBSD',
    packages=find_packages(exclude=["*.__old", "*.tests"]),
    include_package_data=True,
    requires=['numpy (>=1.11)',
              'scipy (>=0.16.1,>=1.0)',
              'sklearn (>=0.17)',
              'six'],
)
