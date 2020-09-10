from os import path
from setuptools import find_namespace_packages, setup
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lambda-learner',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=["Programming Language :: Python :: 3.7",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved"],
    license='BSD-2-CLAUSE',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'numpy >= 1.14',
        'scipy >= 1.0.0',
        'scikit-learn >= 0.18.1',
        'typing-extensions >= 3.7.4',
    ],
    tests_require=[
        'pytest',
    ]
)
