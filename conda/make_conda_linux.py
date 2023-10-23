import yaml
import os
import sys

sys.path = [os.path.join(os.path.dirname(os.path.realpath(__file__)), '')] + sys.path

data = {
    "package": {
        "name": "cgeccore"
        "version": "1.5.6"
    },
    "source": {
        "url": "https://files.pythonhosted.org/packages/24/f0/f4507b608865e56757f80000c34405c8a43e973e888e11e6bdc18fe47ce1/cgecore-1.5.6.tar.gz",
    },
    "build": {
        "number": 0,
        "noarch": "python",
        "script": "{{ PYTHON }} -m pip install . --no-deps --ignore-installed -vv"
    },
    "requirements": {
        "host": [
              "pip",
              "python"
        ],
        "run": [
            "python",
            "biopython"
        ],
        "test": [
            "cgecore",
            "cgecore.blaster",
            "cgecore.organisminfo",
            "cgecore.alignment",
            "cgecore.argumentparsing",
            "cgecore.cgefinder",
            "cgecore.cmdline",
            "cgecore.utility"
        ]
    },
    "about": {
        "home": "https://bitbucket.org/genomicepidemiology/cge_core_module",
        "license": "Apache-2.0",
        "license_family": "Apache",
        "summary": "Center for Genomic Epidemiology Core Module",
        "dev_url": "https://bitbucket.org/genomicepidemiology/cge_core_module"
    }
    }

# Convert the data to YAML and print it
os.system('mkdir conda')
yaml_str = yaml.dump(data, sort_keys=False)

with open('conda/meta.yaml.template', 'w') as f:
    f.write(yaml_str)
