from setuptools import setup

setup(name='mintyper',
      version='1.0.2',
      description='mintyper: an outbreak-detection method for accurate and rapid SNP typing of clonal clusters with noisy long reads',
      url='https://bitbucket.org/genomicepidemiology/mintyper',
      author='Malte Hallgren',
      scripts=['bin/mintyper'],
      author_email='malhal@food.dtu.dk',
      license='Apache 2.0',
      packages='mintyper',
      include_package_data='True',
      zip_safe='False',
      python_requires='>=3.6',
      )