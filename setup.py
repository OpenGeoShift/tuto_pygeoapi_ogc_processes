from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='GeodataValidator',
    version='0.1.0',
    author='OpenGeoShift',
    author_email='contact@opengeoshift.com',
    license='UNLICENSED',
    description='GeodataValidator is a Python package to validate geospatial data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    test_suite='tests',
    python_requires='>=3.6',
    install_requires=read('requirements.txt').splitlines(),
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',

    ]
)