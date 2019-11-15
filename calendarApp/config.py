import yaml

settings = dict


def init(yaml_file_name):
    global settings
    with open(yaml_file_name, 'r') as yml_file:
        settings = yaml.load(yml_file, Loader=yaml.FullLoader)


def get_setting(name, default=None):
    try:
        return settings.get(name, default)
    except TypeError:
        return default


def add_setting(key, value):
    if key is not None:
        settings[key] = value
