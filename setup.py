#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import codecs

from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

def read(filename):
  with codecs.open(os.path.join(cwd, filename), 'rb', 'utf-8') as h:
    return h.read()

metadata = read(os.path.join(cwd, 'doukan', '__init__.py'))

def extract_metaitem(meta):
  # swiped from https://hynek.me 's attr package
  meta_match = re.search(r"""^__{meta}__\s+=\s+['\"]([^'\"]*)['\"]""".format(meta=meta), 
                         metadata, re.MULTILINE)
  if meta_match:
    return meta_match.group(1)
  raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))


if __name__ == '__main__':
  setup(
    name='doukan',
    version=extract_metaitem('version'),
    description=extract_metaitem('description'),
    long_description=read('README.md'),
    author=extract_metaitem('author'),
    author_email=extract_metaitem('email'),
    maintainer=extract_metaitem('author'),
    maintainer_email=extract_metaitem('email'),
    url=extract_metaitem('url'),
    download_url=extract_metaitem('download_url'),
    license=extract_metaitem('license'),
    platforms=['Any'],
    install_requires=[
      'click',
      'colorama',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    py_modules=['doukan'],
    entry_points='''
      [console_scripts]
      doukan=doukan:cli
    ''',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Operating System :: OS Independent',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ]
  )
