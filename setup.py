from distutils.core import setup
setup(
  name = 'telecheck',
  packages = ['telecheck'],
  version = '0.1',
  description = 'Telegram ID Recommender',
  long_description='''Telegram ID Recommender''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/telecheck',
  download_url = 'https://github.com/sepandhaghighi/telecheck/tarball/v0.1',
  keywords = ["Telegram","python","ID","Username","User","Recommender","Generator"],
  install_requires=[
      'art',
	  'codecov',
      'requests',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
    ],
  license='MIT',
)
