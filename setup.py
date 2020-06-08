from setuptools import setup

setup(
    name='esr2',
    version=0.8,
    url='https://github.com/patroqueeet/python-esr2',
    author='patroqueeet',
    author_email='patroqueeet@gmail.com',
    description=('Read swiss BESR / v11 files'),
    license='GPL',
    packages=['esr2', 'esr.utils'],
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
