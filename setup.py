from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='PREFACTOR_LOFAR_pipeline',
      version='0.1',
      description='',
      long_description=readme(),
      packages=['PREFACTOR_LOFAR_pipeline'],
      include_package_data=True,
      zip_safe=True)
