# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pathlib import Path
import logging


def get_requirements():
    requirements_path = Path(__file__).parent / 'requirements.txt'
    logging.info('Requirements path: {}'.format(requirements_path.resolve()))
    with open(str(requirements_path)) as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='opem',
    packages=['opem', 'opem.Static', 'opem.Dynamic', 'opem.Test'],
    version='0.8',
    description='Open Source PEM Cell Simulation Tool',
    long_description='''
  Modeling and simulation of proton-exchange membrane fuel cells (PEMFC) may work as a powerful tool in the Research &
  development of renewable energy sources. The Open-Source PEMFC Simulation Tool (OPEM) is a modeling tool for
  evaluating the performance of proton exchange membrane fuel cells. This package is a combination of models
  (static/dynamic) that predict the optimum operating parameters of PEMFC. OPEM contained generic models that
  will accept as input, not only values of the operating variables such as anode and cathode feed gas, pressure
  and compositions, cell temperature and current density, but also cell parameters including the active area and
  membrane thickness. In addition, some of the different models of PEMFC that have been proposed in the OPEM,
  just focus on one particular FC stack, and some others take into account a part or all auxiliaries such as
  reformers. OPEM is a platform for collaborative development of PEMFC models.''',
    author='Sepand Haghighi,Kasra Askari,Sarmin Hamidi,Mohammad Mahdi Rahimi',
    author_email='opem@ecsim.ir',
    url='https://github.com/ecsim/opem',
    download_url='https://github.com/ecsim/opem/tarball/v0.8',
    keywords="OPEM PEM FC CELL Fuel-Cell Chemistry",
    project_urls={
        'Webpage': 'http://opem.ecsim.ir',
        'Say Thanks!': 'https://saythanks.io/to/ecsim',
        'Source': 'https://github.com/ecsim/opem',
    },
    platforms=["any"],
    install_requires=get_requirements(),
    python_requires='>=3.3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
    license='MIT',
)
