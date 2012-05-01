'''
Basic setup/install script for pyconometrics

Created on Aug 17, 2010
@author: Peter Harrington
peter.b.harrington@gmail.com
'''
from distutils.core import setup
setup(name='pyconometrics',
      version='0.1',
      description='Python Econometrics Utilities',
      author='Peter Harrington',
      author_email='peter.b.harrington@gmail.com',
      url='https://github.com/pbharrin/pyconometrics',
      packages=['pyconometrics'],
      package_dir = {'pyconometrics': 'src'},
     )
