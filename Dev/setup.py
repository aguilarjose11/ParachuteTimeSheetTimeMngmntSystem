from distutils.core import setup, Extension
setup(name = 'devdelta', version = '1.0.0.0',  \
   ext_modules = [Extension('devdelta', ['devdelta.cpp'])])
