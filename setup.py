from setuptools import setup, find_packages

setup(
    name='pluribus',
    version='0.0.1',
    description='A pure-python highly-distributed MapReduce cluster.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='me@jamessocol.com',
    url='https://github.com/jsocol/pluribus',
    license='Apache v2.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pluribus = pluribus._main:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
