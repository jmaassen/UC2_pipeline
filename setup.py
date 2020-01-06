from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='UC2_pipeline',
      version='0.1',
      description='',
      long_description=readme(),
      packages=['UC2_pipeline'],
      include_package_data=True,
      zip_safe=True)
