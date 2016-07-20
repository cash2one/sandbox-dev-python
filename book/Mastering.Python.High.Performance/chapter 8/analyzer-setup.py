from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Analyzer app',
  ext_modules = cythonize("<analyzer></analyzer>_cython.pyx"),
)