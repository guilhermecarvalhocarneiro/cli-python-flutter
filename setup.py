"""

Flutter setup.

Instalar o Flutter CLI na máquina

"""

from setuptools import setup

setup(
    name='flutter_cli',
    version='0.0.1', 
    packages=['cli_flutter', 'snippets'],
    entry_points = {
        'console_scripts': [
            'flutter_cli = cli_flutter'
        ]
    }
)
