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
        "url": "https://bitbucket.org/genomicepidemiology/plasmidfinder/get/2.1.6.tar.gz",
    },
    "build": {
        "number": 0,
        "script": "{{ PYTHON }} -m pip install . --no-deps --ignore-installed -vvv"
    },
    "requirements": {
        "host": [
            "python",
            "wget",
            "kma"
        ],
        "run": [
            "python",
            "wget",
            "biopython",
            "tabulate",
            "cgecore",
            "blast"
        ]
    },
    "about": {
        "home": "https://github.com/genomicepidemiology/plasmidfinder",
        "summary": "plasmidfinder test.",
        "license": "Apache-2.0"
    }
}

# Convert the data to YAML and print it
os.system('mkdir conda_1')
yaml_str = yaml.dump(data, sort_keys=False)

with open('conda_1/meta.yaml', 'w') as f:
    f.write(yaml_str)