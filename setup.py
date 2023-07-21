from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
if __name__ == '__main__':
setup(
    name='evergreen',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/evergreen',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['scripts/parallel_snp_pipeline.py'],
    author_email='malhal@food.dtu.dk',
    description='parallel_snp_pipeline.py -h',
)