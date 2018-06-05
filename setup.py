"""Python setup script for SPaircraft"""
from setuptools import setup

description = """
Signomial programming compatible models for commercial aircraft design. 
Requires installations of `GPkit <https://github.com/convexengineering/gpkit>`_
and `turbofan <https://github.com/convexengineering/turbofan>`_. 
`Documentation <http://spaircraft.readthedocs.io/en/latest/>`_
"""

setup(name = 'SPaircraft',
	version = '0.0.0',
	description = description,
    url='https://github.com/convexengineering/SPaircraft',
    author='Berk Ozturk, Martin York',
    author_email='bozturk@mit.edu',
    license='MIT',
    packages=[],
    install_requires = ['turbofan', 'gpkit'])
