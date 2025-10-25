from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

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
    install_requires=requirements,
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
