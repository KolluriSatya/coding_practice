from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
 setup(
    name='evergreen',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    url='https:https://github.com/KolluriSatya/coding_practice/tree/evergreen',
    license='',
    install_requires=(),
    author='Malte B. Hallgren',
    scripts=['scripts/'],
    description='evergreen',
)