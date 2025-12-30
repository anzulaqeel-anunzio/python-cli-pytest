# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from setuptools import setup, find_packages

setup(
    name='python-cli-scaffold',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'mycli=mypackage.cli:main',
        ],
    },
    author='Anzul Aqeel',
    description='A scaffold for Python CLI tools',
)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
