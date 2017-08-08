from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='libwebpay',
      version=version,
      description="Bibliotecas dpara integrar WebPay de Transbank",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mario Castro Squella',
      author_email='mario.castro.squella@gmail.com',
      url='https://github.com/MarcAstr0/',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'suds==0.4-SNAPSHOT',
          'py-wsse==0.1-SNAPSHOT'
      ],
      dependency_links=[
            'git+https://github.com/MarcAstr0/suds.git#egg=suds-0.4-SNAPSHOT',
            'git+https://github.com/MarcAstr0/py-wsse.git#egg=py-wsse-0.1-SNAPSHOT'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
