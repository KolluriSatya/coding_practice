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
        "url": "https://files.pythonhosted.org/packages/71/e5/0f3c76f148024cb4f97f3a219247b62f9d9c8c2ac09c45fa2f9d20c8fa12/blast-0.3.0.tar.gz",
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