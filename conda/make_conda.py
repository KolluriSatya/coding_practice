import yaml
import os
import sys

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '')] + sys.path

data = {
    "package": {
        "name": "plasmidfinder",
        "version": "2.1.6"
    },
    "source": {
        "url": "https://github.com/genomicepidemiology/plasmidfinder/archive/refs/tags/2.1.6.tar.gz"
    },
    "build": {
        "number": 0,
        "noarch": "generic",
    },
    "requirements": {
        "host": [
            "python >=3.5",
            "kma",
            "wget"
        ],
        "run": [
            "python >=3.5",
            "biopython",
            "kma",
            "blast",
            "cgecore",
            "tabulate"
        ]
    },
    "about": {
        "home": "https://github.com/genomicepidemiology/plasmidfinder",
        "summary": "plasmidfinder test.",
        "license": "Apache-2.0"
    }
}

# Convert the data to YAML and print it
os.system('mkdir conda')
yaml_str = yaml.dump(data, sort_keys=False)

with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)