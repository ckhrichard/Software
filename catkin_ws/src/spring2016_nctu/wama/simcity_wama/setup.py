## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
#from simcity.util import *

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['simcity_wama'],
    package_dir={'': 'include'},
)

setup(**setup_args)
