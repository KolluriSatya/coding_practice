import ruamel.yaml as yaml

# Create an ordered dictionary for each section
package = yaml.comments.CommentedMap()
package['name'] = 'ccphylo'

with open('version.h', 'r') as f:
    for line in f:
        if line.startswith('#define'):
            package['version'] = line.split()[2].replace("\"", "")

source = yaml.comments.CommentedMap()
source['url'] = 'https://bitbucket.org/genomicepidemiology/{}/get/{}.tar.gz'.format(package['name'], package['version'])

build = yaml.comments.CommentedMap()
build['number'] = 0

requirements = yaml.comments.CommentedMap()
requirements['build'] = ['make', '{{ compiler(\'c\') }}']
requirements['host'] = ['zlib']
requirements['run'] = ['zlib']

about = yaml.comments.CommentedMap()
about['home'] = 'https://bitbucket.org/genomicepidemiology/ccphylo'
about['summary'] = 'CCPhylo is a software suite designed to easen phylogenetic analysis based on alignments from KMA. Neighbor-Joining can be run without KMA alignments, if a Phylip distance matrix is given using "ccphylo tree".'
about['license'] = 'Apache-2.0'

extra = yaml.comments.CommentedMap()
identifiers = yaml.comments.CommentedMap()
identifiers['doi'] = '10.1093/bioinformatics/btac774'
identifiers['doi'] = '10.1093/biomethods/bpab008'
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