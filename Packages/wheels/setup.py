from setuptools import setup, find_packages

setup(
        name = 'redshift_connector',
        version = '1.1',
        author = 'Esaú Reyes',
        packages = ['redshift_connector'], #pfind_packages()
        install_requires=['scramp']
        )
