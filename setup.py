#StudentUnderground/setup.py
from setuptools import setup

setup(name='JayD3e',
      version='0.1dev',
      description='A web-based note takeing application',
      long_description='',
      install_requires=['pyramid',
                        'mako',
                        'sqlalchemy',
                        'pyramid_handlers',
                        'MySQL-python',
                        'weberror',
                        'nose',
                        'coverage',
                        'markdown'],
      url='http://localhost',
      packages=['jayd3e'],
      test_suite='jayd3e',
      entry_points = """\
      [paste.app_factory]
      main = jayd3e:main
      """,
      )
