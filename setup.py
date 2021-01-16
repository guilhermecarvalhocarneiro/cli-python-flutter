"""
Flutter setup.

Instalar o Flutter CLI na terminal.
"""

from setuptools import setup, find_packages

setup(
    name='flutter_cli',
    version='0.3.2',
    packages=['cli_flutter', 'snippets'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flutter_cli = cli_flutter'
        ]
    }
)