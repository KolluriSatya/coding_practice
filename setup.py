from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(_file_).parent
long_description = (this_directory / "README.md").read_text()

setup(name='mintyper',
      version='1.0.2',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/genomicepidemiology/mintyper',
      packages=find_packages(),
      data_files=[],
      author='Malte Hallgren',
      scripts=['bin/mintyper'],
      author_email='malhal@food.dtu.dk',
      license='Apache 2.0',
      packages='mintyper',
      include_package_data='True',
      zip_safe='False',
      python_requires='>=3.6',
      )
