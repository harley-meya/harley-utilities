from setuptools import setup

VERSION = '1.0.0'

description = (
    "Harley's first package!"
)

install_requires = []

packages = [
    'harley_utilities' # Replace with the name of your Python module.
]

setup(
    name='harley-utilities',
    version=VERSION,
    description=description,
    url='https://github.com/harley-meya/harley-utilities',
    author='Harley Pellowe',
    author_email='harley@meya.ai',
    license='None',
    packages=packages,
    install_requires=install_requires,
    zip_safe=False)