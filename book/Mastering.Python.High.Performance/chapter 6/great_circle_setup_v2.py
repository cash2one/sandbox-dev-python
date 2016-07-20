from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Great Circle module v2',
  ext_modules = cythonize("great_circle_cy_v2.pyx"),
)