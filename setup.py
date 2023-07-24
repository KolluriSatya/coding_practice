from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent


setup(
    name='evergreen',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/evergreen',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['scripts/parallel_snp_pipeline.py'],
    description='evergreen',
)