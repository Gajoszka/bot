import yaml

_cfg = {}


def getCfg(name):
    if cfg is None:
     with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
