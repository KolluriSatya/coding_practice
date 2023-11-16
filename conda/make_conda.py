import ruamel.yaml as yaml
import io
import sys

# Create an ordered dictionary for each section
package = yaml.comments.CommentedMap()
package['name'] = 'plasmidfinder'

# Load your YAML content
with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)

source = yaml.comments.CommentedMap()
source['url'] = 'https://bitbucket.org/genomicepidemiology/{}/get/2.1.6.tar.gz'.format(package['name'])

build = yaml.comments.CommentedMap()
build['number'] = 0
build['noarch'] = 'python'

requirements = yaml.comments.CommentedMap()
requirements['build'] = ['python']
requirements['host'] = ['python', 'wget', 'biopython', 'tabulate', 'cgecore']
requirements['run'] = ['python', 'wget', 'biopython', 'tabulate', 'cgecore']

about = yaml.comments.CommentedMap()
about['home'] = 'https://bitbucket.org/genomicepidemiology/plasmidfinder'
about['summary'] = 'plasmidfinder test.'
about['license'] = 'Apache-2.0'

extra = yaml.comments.CommentedMap()
identifiers = yaml.comments.CommentedMap()
identifiers['doi'] = 'doi:10.1093/bioinformatics/btac774'
extra['identifiers'] = identifiers

# Create a dictionary for the entire YAML content
data = yaml.comments.CommentedMap()
data['package'] = package
data['source'] = source
data['build'] = build
data['requirements'] = requirements
data['about'] = about
data['extra'] = extra

#create data outstream
output_stream = io.StringIO()


# Serialize the data to YAML and print it
yaml = yaml.YAML(typ='unsafe', pure=True)

# Dump the data using the YAML instance into the output stream
yaml.dump(data, output_stream)

# Get the YAML string from the output stream
yaml_str = output_stream.getvalue().replace("\"{{", "{{").replace("}}\"", "}}")
print(yaml_str)

with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)