from setuptools import setup, find_packages

setup(
    name='Servmon',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Flask-Script', 'Flask-Cors', 'pymongo', 'pytest', 'sphinx', 'sphinxcontrib-httpdomain']
)
