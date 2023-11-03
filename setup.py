from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='your-package-name',
    version='1.0.0',
    description='Your package description',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/baxromov/JIGI.git',
    packages=['your_package'],
    install_requires=required,  # This includes the dependencies from requirements.txt
)
