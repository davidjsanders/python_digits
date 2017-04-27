from setuptools import setup

setup(name='python_digits',
      version='0.3',
      description='Python digits (integers between 0 and 9)',
      url='https://github.com/dsandersAzure/python_digits',
      author='David Sanders',
      author_email='dsanderscanadanospam@gmail.com',
      license='Apache License 2.0',
      packages=['python_digits'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
