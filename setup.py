from setuptools import setup, find_packages

setup(
    name='evergreen',
    packages=find_packages(),
    install_requires=[
        'anaconda-client',
        'python=2.7',
        'scipy',
        'numpy',
        'ete3',
        'joblib'
        ],
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/evergreen',
    license='',
    author='Malte B. Hallgren',
    scripts=['scripts/'],
    author_email='malhal@food.dtu.dk',
    description='evergreen, parallel_snp_pipeline',
)


