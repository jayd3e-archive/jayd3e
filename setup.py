#StudentUnderground/setup.py
from setuptools import setup

setup(name='JayD3e',
      version='0.1dev',
      description='My personal blog.',
      long_description='',
      install_requires=['pyramid',
                        'mako',
                        'sqlalchemy',
                        'pyramid_handlers',
                        'MySQL-python',
                        'waitress',
                        'nose',
                        'coverage',
                        'markdown',
                        'pysqlite'],
      url='http://localhost',
      packages=['jayd3e'],
      test_suite='jayd3e.tests',
      entry_points = """\
      [paste.app_factory]
      main = jayd3e:main
      """,
      )
