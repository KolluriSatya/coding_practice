import ruamel.yaml as yaml

# Create an ordered dictionary for each section
package = yaml.comments.CommentedMap()
package['name'] = 'cgecore'
package['version'] = '1.5.6'

source = yaml.comments.CommentedMap()
source['url'] = 'https://files.pythonhosted.org/packages/65/40/34c5fe13ef544ed241fb2dd621d0160c065652a0575137b5ad66e5b279c8/ruamel.yaml-0.18.2.tar.gz'

build = yaml.comments.CommentedMap()
build['number'] = 0
build['noarch'] = 'python'

requirements = yaml.comments.CommentedMap()
requirements['host'] = ['python', 'pip']
requirements['run'] = ['python', 'biopython']

about = yaml.comments.CommentedMap()
about['home'] = 'https://bitbucket.org/genomicepidemiology/cgecore'
about['summary'] = 'cgecore test.'
about['license'] = 'Apache-2.0'

extra = yaml.comments.CommentedMap()
identifiers = yaml.comments.CommentedMap()
extra['identifiers'] = identifiers

# Create a dictionary for the entire YAML content
data = yaml.comments.CommentedMap()
data['package'] = package
data['source'] = source
data['build'] = build
data['requirements'] = requirements
data['about'] = about
data['extra'] = extra

# Serialize the data to YAML and print it
yaml_str = yaml.dump(data, Dumper=yaml.RoundTripDumper).replace("\"{{", "{{").replace("}}\"", "}}")
print(yaml_str)

with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)