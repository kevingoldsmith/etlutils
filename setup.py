from setuptools import setup

setup(name='etlutils',
      version='0.1',
      description='utilities functions for egoanalytics projects',
      author='Kevin Goldsmith',
      author_email='kevin@kevingoldsmith.com',
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
      python_requires=['>=3.6'],
      packages=['etlutils'])
