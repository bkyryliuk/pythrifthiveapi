from setuptools import setup, find_packages

version = '0.1.1.0'

setup(
    name='pythrifthiveapi',
    description=(
        "Thrift Schema and python client for the Hive Thrift API."),
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'future',
        'thrift>=0.8.0',
        'sasl>=0.1.3',
    ],
    author='Bogdan Kyryliuk',
    author_email='b.kyryliuk@gmail.com',
    url='https://git.musta.ch/bkyryliuk/pythrifthiveapi',
    download_url=(
        'https://github.com/bkyryliuk/pythrifthiveapi/tarball/' + version),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)