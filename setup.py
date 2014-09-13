from setuptools import setup, find_packages
import os

version = open(os.path.join("rfd15", "theme", "version.txt")).read().strip()

setup(name='rfd15.theme',
      version=version,
      description="Diazo theme for Plone rfd15",
      long_description=open(os.path.join("docs", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        ],
      keywords='',
      author='Paul Roeland',
      author_email='paulroeland@rozefilmdagen.nl',
      url='http://www.rozefilmdagen.nl/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rfd15'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
            'test': [
                    'plone.app.testing',
                ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
