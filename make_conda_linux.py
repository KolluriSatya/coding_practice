import yaml
import os
import sys

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '')] + sys.path
data = {
    "package": {
        "name": "blast",
        "version": "0.3.0"
    },
    "source": {
        "url": "https://bitbucket.org/genomicepidemiology/blaster/src/master/",
    },
    "build": {
        "number": 0,
        "script": "{{ PYTHON }} -m pip install . --no-deps --ignore-installed -vvv"
    },
    "requirements": {
        "host": [
            "python"
        ],
        "run": [
            "python"
        ]
    },
    "about": {
        "home": "https://github.com/genomicepidemiology/blaster",
        "summary": "blast test.",
        "license": "Apache-2.0"
    }
}

# Convert the data to YAML and print it
os.system('mkdir conda')
yaml_str = yaml.dump(data, sort_keys=False)

with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)