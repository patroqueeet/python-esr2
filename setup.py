import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

setup(
    name='ESR',
    version=0.2,
    url='https://github.com/patroqueeet/python-esr2',
    author='patroqueeet',
    author_email='patroqueeet@gmail.com',
    description=('Read swiss BESR / v11 files'),
    license='GPL',
    packages='',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
