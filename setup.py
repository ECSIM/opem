# -*- coding: utf-8 -*-
from setuptools import setup
setup(
  name = 'opem',
  packages = ['opem','opem.Static','opem.Dynamic'],
  version = '0.6',
  description = 'Open Source PEM Cell Simulation Tool',
  long_description='''The Open-Source PEMFC Simulation Tool (Opem) is an open-source mathematical simulation package for polymer electrolyte fuel cells.
  It contains a database of physical phenomena equations,  and kinetics mathematical models in order to perform static/dynamic analysis of PEMFC.
  The goal of the software is to prepare a platform for collaborative development of  PEMFC mathematical models.''',
  author = 'Sepand Haghighi,Kasra Askari,Sarmin Hamidi,Mohammad Mahdi Rahimi',
  author_email = 'opem@ecsim.ir',
  url = 'https://github.com/ecsim/opem',
  download_url = 'https://github.com/ecsim/opem/tarball/v0.6',
  keywords = "OPEM PEM FC CELL Fuel-Cell Chemistry",
  project_urls={
    'Webpage': 'http://opem.ecsim.ir',
    'Say Thanks!': 'https://saythanks.io/to/ecsim',
    'Source': 'https://github.com/ecsim/opem',
     },
  install_requires=[
      'art',
	  'codecov',
      'requests',
      ],
  python_requires='>=3.3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
  license='MIT',
)
