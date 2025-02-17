import os
import setuptools
import sys

# Suyog
import numpy as np
# class NumpyImport:
#   def __repr__(self):
#     import numpy as np

#     return np.get_include()

#   __fspath__ = __repr__
np_path = np.get_include()

def read(fname):
  with open(os.path.join(os.path.dirname(__file__), fname), 'rt') as f:
    return f.read()

def requirements():
  with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'rt') as f:
    return f.readlines()

# NOTE: If cc3d.cpp does not exist:
# cython -3 --fast-fail -v --cplus cc3d.pyx

extra_compile_args = []
if sys.platform == 'win32':
  extra_compile_args += [
    '/std:c++11', '/O2'
  ]
else:
  extra_compile_args += [
    '-std=c++11', '-O3'
  ]

if sys.platform == 'darwin':
  extra_compile_args += [ '-stdlib=libc++', '-mmacosx-version-min=10.9' ]

setuptools.setup(
  name="connected-components-3d",
  version="3.12.2",
  setup_requires=['pbr', 'numpy', 'cython'],
  install_requires=['numpy'],
  python_requires=">=3.7,<4.0",
  ext_modules=[
    setuptools.Extension(
      'cc3d',
      sources=[ 'cc3d.pyx' ],
      language='c++',
      # include_dirs=[ NumpyImport() ], # Suyog
      include_dirs=[ np_path ],  # Suyog
      extra_compile_args=extra_compile_args,
    )
  ],
  author="William Silversmith",
  author_email="ws9@princeton.edu",
  packages=setuptools.find_packages(),
  package_data={
    'cc3d': [
      'LICENSE',
    ],
  },
  description="Connected components on 2D and 3D images. Supports multiple labels.",
  long_description=read('README.md'),
  long_description_content_type="text/markdown",
  license = "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
  keywords = "connected-components CCL volumetric-data numpy connectomics image-processing biomedical-image-processing decision-tree union-find sauf bbdt 2d 3d",
  url = "https://github.com/seung-lab/connected-components-3d/",
  classifiers=[
    "Intended Audience :: Developers",
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering",
    "Intended Audience :: Science/Research",
    "Operating System :: POSIX",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows :: Windows 10",
  ],  
)


