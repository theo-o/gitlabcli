from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


def read_long_description():
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()


def read_short_description():
    import labcli
    return labcli.__description__


def read_version():
    import labcli
    return labcli.__version__


setup(name='gitlab-cli',
      version='0.1.0',
      description=read_short_description(),
      long_description=read_long_description(),
      long_description_content_type='text/markdown',
      url='https://github.com/theo-o/gitlab-cli',
      author='Theo Ouzhinski',
      author_email='touzhinski@gmail.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3'
          ' or later (GPLv3+)',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='gitlab development VC git',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      entry_points={
        'console_scripts': [
            'cli=labcli.cli:main']}
      )
