import yaml
import os
import sys

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '')] + sys.path

data = {
    "package": {
        "name": "cgecore",
        "version": version.__version__
    },
    "source": {
        "url": "https://github.com/genomicepidemiology/cgecore/archive/refs/tags/{}.tar.gz".format(version.__version__),
    },
    "build": {
        "number": 0,
        "noarch": "python",
        "script": "{{ PYTHON }} -m pip install . --no-deps --ignore-installed -vvv"
    },
    "requirements": {
        "host": [
            "python",
            "pip"
        ],
        "run": [
            "python",
            "pip"
        ]
    },
    "about": {
        "home": "https://github.com/genomicepidemiology/cgecore",
        "summary": "cgecore test.",
        "license": "Apache-2.0"
    }
}

# Convert the data to YAML and print it
os.system('mkdir conda')
yaml_str = yaml.dump(data, sort_keys=False)

with open('conda/meta.yaml', 'w') as f:
    f.write(yaml_str)