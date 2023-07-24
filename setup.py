from setuptools import setup
if __name__ == '__main__':

setup(
    name='evergreen',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/evergreen',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['bin/parallel_snp_pipeline.py'],
    description='evergreen',
)