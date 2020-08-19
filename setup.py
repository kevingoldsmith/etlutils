from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='etlutils',
      version='0.2.2',
      description='utilities functions for etl projects',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Kevin Goldsmith',
      author_email='github@kevingoldsmith.com',
      url='https://github.com/kevingoldsmith/etlutils',
      license='MIT',
      keywords='development etl extract transform load',
      project_urls={
            'Source': 'https://github.com/kevingoldsmith/etlutils'
      },
      classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
      ],
      install_requires=['python-dateutil>=2.8.1'],
      python_requires='>=3.6',
      packages=['etlutils'])
