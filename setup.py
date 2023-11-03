from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='jigi',
    version='1.0.6',
    description='JIGI',
    author='Baxromov Shahzodbek',
    author_email='baxromov.shahzodbek@gmail.com',
    url='https://github.com/baxromov/JIGI.git',
    packages=find_packages(),
    install_requires=required
)
