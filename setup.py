from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='flankophile',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/flankophile',
    license='',
    install_requires=(),
    author=' Alix Vincent Thorn',
    scripts=['bin/'],
    author_email='alvit@food.dtu.dk',
    description='Flankophile, Snakemake',
)