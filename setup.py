from setuptools import find_packages, setup


import numpy as np

classes = """
    Development Status :: 1 - Pre-Alpha
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='horseshoe_analyses',
      version='1.0',
      license='BSD-3-Clause',
      description='Horseshoe Analyses',
      long_description='Horseshoe Analyses',
      author="horseshoe development team",
      author_email="jamietmorton@gmail.com",
      maintainer="horshoe development team",
      maintainer_email="jamietmorton@gmail.com",
      packages=find_packages(),
      include_dirs=[np.get_include()],
      install_requires=[
          'scikit-bio', 'numpy', 'biom-format', 'pandas', 
          'gneiss', 'matplotlib', 'seaborn', 'scipy'
      ],
      classifiers=classifiers,
      package_data={
          }
      )
