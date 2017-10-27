
from distutils.core import setup, Extension

module_servo = Extension('servo', include_dirs = ['usr/include'], libraries = ['boost_python'], library_dirs = ['usr/lib'], sources = ['servo_gymbal.cpp'])
setup(name = 'servo', version = '0.1', description = 'Test  version of Servo Movement', ext_modules = [module_servo])
