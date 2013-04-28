#StudentUnderground/setup.py
from setuptools import setup

entry_points = """\
    [paste.app_factory]
    main = jayd3e:main
"""

setup(name='jayd3e',
      version='0.1dev',
      description='My personal blog.',
      long_description='',
      install_requires=['pyramid==1.3',
                        'mako',
                        'sqlalchemy',
                        'psycopg2',
                        'waitress',
                        'nose',
                        'coverage',
                        'markdown',
                        'pysqlite'],
      url='http://localhost',
      packages=['jayd3e'],
      test_suite='jayd3e.tests',
      entry_points=entry_points
      )
