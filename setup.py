from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from sysconfig import get_paths
import os, sys
import warnings
import subprocess

if True:
    # precompiled library from:
    # https://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.21/libusb-1.0.21.7z/download
    # need visualstudio prior to 2013, for this precompiled library
    # therefore ideally before even python installation, install vs
    # currently used link i have to vs2012, but could use older 2008 at http://download.microsoft.com/download/A/5/4/A54BADB6-9C3F-478D-8657-93B3FC9FE62D/vcsetup.exe
    # if setup.py still appears to be using a newer version, can hack it:
    # https://www.ibm.com/developerworks/community/blogs/jfp/entry/Installing_Cython_On_Anaconda_On_Windows?lang=en
    # https://sleangao.wordpress.com/2015/03/24/using-cython-under-windows-7-with-msvc-compiler/
    warnings.warn('Setup params not yet fully tested for Windows.')

    libusb_incl = [os.path.join('pseyepy', 'ext', 'win', 'include', 'libusb-1.0')]
    libusb_libpath = 'pseyepy/ext/win/lib'
    libs = ['libusb-1.0']

### setup params
os.environ["CC"]= "g++"
srcs = ['pseyepy/src/ps3eye.cpp','pseyepy/src/ps3eye_capi.cpp','pseyepy/cameras.pyx']
extensions = [  Extension('pseyepy.cameras',
                srcs, 
                language='c++',
                extra_compile_args=['-std=c++11'],
                extra_link_args=['-std=c++11'],
                include_dirs=['pseyepy\\ext\\win\\include\\', 'pseyepy\\src'],
                library_dirs=[libusb_libpath],
                libraries=libs,
            )]

### run setup
setup(  name='pseyepy',
        version='0.0',
        description='pseyepy camera package  SETUP FIXED BY MirageDev',
        author='Ben Deverett',
        author_email='deverett@princeton.edu',
        url='https://github.com/bensondaled/pseyepy',
        packages=['pseyepy'],
        package_data={'pseyepy': ['cameras.pyx']},
        ext_modules=cythonize(extensions),)
