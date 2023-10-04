from setuptools import setup, find_packages

setup(
    name='cuCKKS',
    description='Python implementations CKKS',
    install_requires=[
        'sympy',
        'pytest',
    ],
    packages=['src','tests', 'util']
)