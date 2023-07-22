import os
from setuptools import setup, find_packages
VERSION = '0.0.1' 
DESCRIPTION = 'ADB wrapper'
LONG_DESCRIPTION = 'Simple ADB wrapper that uses command line. I am unsure if its cross platform'
setup(
       # the name must match the folder name 'verysimplemodule'
        name="adbpy", 
        version=VERSION,
        author="Daniel",
        author_email="",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'ADB', 'Android'],
        classifiers= [
            "Development Status :: Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)