from setuptools import setup
setup(
    name='flankophile',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https://https://github.com/genomicepidemiology/flankophile',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['bin/'],
    author_email='malhal@food.dtu.dk',
    description='flankophile snakamake',
)