from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='plasmidfinder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://github.com/genomicepidemiology/plasmidfinder',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['plasmidfinder.py'],
    author_email='malhal@food.dtu.dk',
    description='plasmidfinder - Plasmidfinder',
)