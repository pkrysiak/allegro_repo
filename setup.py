# -*- coding:UTF-8 -*-

from setuptools import setup

setup(name = 'Allegro app',
      version = '1.0',
      author = 'Paweł Krysiak',
      author_email = 'pawel.krysiak@stxnext.pl',
      packages = ['allegro','tests'],
      install_requires = ['mechanize', 'beautifulsoup4'],
      test_suite='tests',
      entry_points = {'console_scripts': ['main = allegro.scripts:main']}
)